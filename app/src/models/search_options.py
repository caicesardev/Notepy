from dataclasses import dataclass

from PySide6.QtGui import QTextDocument


@dataclass(frozen=True)
class SearchOptions:
    text: str
    case_sensitive: bool = False
    whole_words: bool = False
    wrap_around: bool = True

    def find_flags(self, backward: bool = False) -> QTextDocument.FindFlag:
        flags = QTextDocument.FindFlag(0)
        if self.case_sensitive:
            flags |= QTextDocument.FindFlag.FindCaseSensitively
        if self.whole_words:
            flags |= QTextDocument.FindFlag.FindWholeWords
        if backward:
            flags |= QTextDocument.FindFlag.FindBackward
        return flags

    def matches(self, candidate: str) -> bool:
        if self.case_sensitive:
            return candidate == self.text
        return candidate.casefold() == self.text.casefold()
