from dataclasses import dataclass
from pathlib import Path

from src.models.file_format import FileFormat
from src.models.line_ending import LineEnding
from src.models.text_encoding import TextEncoding

EDITOR_LINE_SEPARATOR = "\n"


@dataclass(frozen=True)
class DecodedText:
    text: str
    file_format: FileFormat


def decode_text(data: bytes) -> DecodedText:
    encoding = detect_encoding(data)
    raw_text = data[len(encoding.byte_order_mark):].decode(encoding.codec, errors="replace")
    line_ending = LineEnding.detect(raw_text, default=FileFormat().line_ending)
    return DecodedText(normalize_line_endings(raw_text), FileFormat(encoding, line_ending))


def encode_text(text: str, file_format: FileFormat) -> bytes:
    content = text.replace(EDITOR_LINE_SEPARATOR, file_format.line_ending.sequence)
    encoding = file_format.encoding
    return encoding.byte_order_mark + content.encode(encoding.codec, errors="replace")


def detect_encoding(data: bytes) -> TextEncoding:
    for encoding in TextEncoding.with_byte_order_mark():
        if data.startswith(encoding.byte_order_mark):
            return encoding
    return TextEncoding.UTF8 if is_valid_utf8(data) else TextEncoding.ANSI


def is_valid_utf8(data: bytes) -> bool:
    try:
        data.decode(TextEncoding.UTF8.codec)
    except UnicodeDecodeError:
        return False
    return True


def normalize_line_endings(text: str) -> str:
    return text.replace("\r\n", EDITOR_LINE_SEPARATOR).replace("\r", EDITOR_LINE_SEPARATOR)


def read_text_file(path: Path) -> DecodedText:
    return decode_text(path.read_bytes())


def write_text_file(path: Path, text: str, file_format: FileFormat) -> None:
    path.write_bytes(encode_text(text, file_format))
