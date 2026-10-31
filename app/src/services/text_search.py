from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QPlainTextEdit

from src.models.search_options import SearchOptions


class TextSearch:
    def __init__(self, editor: QPlainTextEdit) -> None:
        self._editor = editor

    def find(self, options: SearchOptions, backward: bool = False) -> bool:
        if not options.text:
            return False
        flags = options.find_flags(backward)
        if self._editor.find(options.text, flags):
            return True
        if not options.wrap_around:
            return False
        return self._find_from_document_edge(options, backward)

    def replace(self, options: SearchOptions, replacement: str) -> bool:
        cursor = self._editor.textCursor()
        if cursor.hasSelection() and options.matches(cursor.selectedText()):
            cursor.insertText(replacement)
        return self.find(options)

    def replace_all(self, options: SearchOptions, replacement: str) -> int:
        if not options.text:
            return 0
        document = self._editor.document()
        flags = options.find_flags()
        edit_cursor = QTextCursor(document)
        edit_cursor.beginEditBlock()
        replacements = 0
        match = document.find(options.text, QTextCursor(document), flags)
        while not match.isNull():
            match.insertText(replacement)
            replacements += 1
            match = document.find(options.text, match, flags)
        edit_cursor.endEditBlock()
        return replacements

    def _find_from_document_edge(self, options: SearchOptions, backward: bool) -> bool:
        edge = QTextCursor.MoveOperation.End if backward else QTextCursor.MoveOperation.Start
        start = QTextCursor(self._editor.document())
        start.movePosition(edge)
        match = self._editor.document().find(options.text, start, options.find_flags(backward))
        if match.isNull():
            return False
        self._editor.setTextCursor(match)
        return True
