import codecs
import tempfile
import unittest
from pathlib import Path

from src.models.file_format import FileFormat
from src.models.line_ending import LineEnding
from src.models.text_encoding import TextEncoding
from src.services.text_codec import decode_text, encode_text, read_text_file, write_text_file


class DecodeTextTest(unittest.TestCase):
    def test_detects_utf8_without_byte_order_mark(self) -> None:
        decoded = decode_text("año\r\ncanción".encode("utf-8"))
        self.assertEqual(decoded.text, "año\ncanción")
        self.assertEqual(decoded.file_format, FileFormat(TextEncoding.UTF8, LineEnding.WINDOWS))

    def test_detects_byte_order_marks(self) -> None:
        cases = {
            TextEncoding.UTF8_BOM: codecs.BOM_UTF8 + "ñ".encode("utf-8"),
            TextEncoding.UTF16_LE: codecs.BOM_UTF16_LE + "ñ".encode("utf-16-le"),
            TextEncoding.UTF16_BE: codecs.BOM_UTF16_BE + "ñ".encode("utf-16-be"),
        }
        for encoding, data in cases.items():
            with self.subTest(encoding=encoding):
                decoded = decode_text(data)
                self.assertEqual(decoded.text, "ñ")
                self.assertIs(decoded.file_format.encoding, encoding)

    def test_falls_back_to_ansi_for_invalid_utf8(self) -> None:
        decoded = decode_text("café €".encode("cp1252"))
        self.assertEqual(decoded.text, "café €")
        self.assertIs(decoded.file_format.encoding, TextEncoding.ANSI)

    def test_detects_line_endings(self) -> None:
        cases = {
            b"a\r\nb": LineEnding.WINDOWS,
            b"a\nb": LineEnding.UNIX,
            b"a\rb": LineEnding.MACINTOSH,
            b"single line": LineEnding.WINDOWS,
        }
        for data, line_ending in cases.items():
            with self.subTest(data=data):
                decoded = decode_text(data)
                self.assertIs(decoded.file_format.line_ending, line_ending)
                self.assertNotIn("\r", decoded.text)


class EncodeTextTest(unittest.TestCase):
    def test_restores_line_endings_and_byte_order_mark(self) -> None:
        file_format = FileFormat(TextEncoding.UTF8_BOM, LineEnding.WINDOWS)
        self.assertEqual(encode_text("a\nb", file_format), codecs.BOM_UTF8 + b"a\r\nb")

    def test_round_trips_every_format(self) -> None:
        text = "Línea 1\nLínea 2 €\n"
        for encoding in TextEncoding:
            for line_ending in LineEnding:
                file_format = FileFormat(encoding, line_ending)
                with self.subTest(file_format=file_format):
                    decoded = decode_text(encode_text(text, file_format))
                    self.assertEqual(decoded.text, text)
                    self.assertIs(decoded.file_format.line_ending, line_ending)

    def test_writes_and_reads_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nota.txt"
            file_format = FileFormat(TextEncoding.UTF16_LE, LineEnding.UNIX)
            write_text_file(path, "hola\nmundo", file_format)
            decoded = read_text_file(path)
            self.assertEqual(decoded.text, "hola\nmundo")
            self.assertEqual(decoded.file_format, file_format)


if __name__ == "__main__":
    unittest.main()
