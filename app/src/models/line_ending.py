from enum import Enum


class LineEnding(Enum):
    WINDOWS = ("\r\n", "Windows (CRLF)")
    UNIX = ("\n", "Unix (LF)")
    MACINTOSH = ("\r", "Macintosh (CR)")

    def __init__(self, sequence: str, label: str) -> None:
        self.sequence = sequence
        self.label = label

    @classmethod
    def detect(cls, text: str, default: "LineEnding") -> "LineEnding":
        for line_ending in cls:
            if line_ending.sequence in text:
                return line_ending
        return default
