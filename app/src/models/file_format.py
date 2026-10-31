from dataclasses import dataclass

from src.models.line_ending import LineEnding
from src.models.text_encoding import TextEncoding


@dataclass(frozen=True)
class FileFormat:
    encoding: TextEncoding = TextEncoding.UTF8
    line_ending: LineEnding = LineEnding.WINDOWS
