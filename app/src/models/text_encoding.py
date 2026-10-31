import codecs
from enum import Enum


class TextEncoding(Enum):
    UTF8 = ("UTF-8", "utf-8", b"")
    UTF8_BOM = ("UTF-8 con BOM", "utf-8", codecs.BOM_UTF8)
    UTF16_LE = ("UTF-16 LE", "utf-16-le", codecs.BOM_UTF16_LE)
    UTF16_BE = ("UTF-16 BE", "utf-16-be", codecs.BOM_UTF16_BE)
    ANSI = ("ANSI", "cp1252", b"")

    def __init__(self, label: str, codec: str, byte_order_mark: bytes) -> None:
        self.label = label
        self.codec = codec
        self.byte_order_mark = byte_order_mark

    @classmethod
    def with_byte_order_mark(cls) -> list["TextEncoding"]:
        return [encoding for encoding in cls if encoding.byte_order_mark]
