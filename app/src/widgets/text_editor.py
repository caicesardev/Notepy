from pathlib import Path

from PySide6.QtCore import QMimeData, Qt, Signal
from PySide6.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent, QFont, QTextCursor, QWheelEvent
from PySide6.QtWidgets import QPlainTextEdit, QWidget

from src.services.zoom import DEFAULT_ZOOM_PERCENT, ZOOM_STEP_PERCENT, clamp_zoom, zoomed_point_size


class TextEditor(QPlainTextEdit):
    zoom_changed = Signal(int)
    files_dropped = Signal(list)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._base_font = QFont(self.font())
        self._zoom_percent = DEFAULT_ZOOM_PERCENT

    @property
    def zoom_percent(self) -> int:
        return self._zoom_percent

    @property
    def cursor_line(self) -> int:
        return self.textCursor().blockNumber() + 1

    @property
    def cursor_column(self) -> int:
        return self.textCursor().positionInBlock() + 1

    @property
    def line_count(self) -> int:
        return self.document().blockCount()

    @property
    def character_count(self) -> int:
        return self.document().characterCount() - 1

    def set_base_font(self, font: QFont) -> None:
        self._base_font = QFont(font)
        self._apply_zoomed_font()

    def set_word_wrap(self, enabled: bool) -> None:
        mode = QPlainTextEdit.LineWrapMode.WidgetWidth if enabled else QPlainTextEdit.LineWrapMode.NoWrap
        self.setLineWrapMode(mode)

    def set_zoom(self, percent: int) -> None:
        clamped = clamp_zoom(percent)
        if clamped == self._zoom_percent:
            return
        self._zoom_percent = clamped
        self._apply_zoomed_font()
        self.zoom_changed.emit(clamped)

    def zoom_in(self) -> None:
        self.set_zoom(self._zoom_percent + ZOOM_STEP_PERCENT)

    def zoom_out(self) -> None:
        self.set_zoom(self._zoom_percent - ZOOM_STEP_PERCENT)

    def reset_zoom(self) -> None:
        self.set_zoom(DEFAULT_ZOOM_PERCENT)

    def go_to_line(self, line_number: int) -> None:
        block = self.document().findBlockByNumber(line_number - 1)
        if block.isValid():
            self.setTextCursor(QTextCursor(block))
            self.centerCursor()

    def delete_forward(self) -> None:
        cursor = self.textCursor()
        cursor.deleteChar()
        self.setTextCursor(cursor)

    def wheelEvent(self, event: QWheelEvent) -> None:
        if not event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            super().wheelEvent(event)
            return
        scroll = event.angleDelta().y()
        if scroll > 0:
            self.zoom_in()
        elif scroll < 0:
            self.zoom_out()
        event.accept()

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if self._contains_local_files(event.mimeData()):
            event.acceptProposedAction()
            return
        super().dragEnterEvent(event)

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        if self._contains_local_files(event.mimeData()):
            event.acceptProposedAction()
            return
        super().dragMoveEvent(event)

    def dropEvent(self, event: QDropEvent) -> None:
        if self._contains_local_files(event.mimeData()):
            event.acceptProposedAction()
            self.files_dropped.emit(self._local_files(event.mimeData()))
            return
        super().dropEvent(event)

    def _apply_zoomed_font(self) -> None:
        font = QFont(self._base_font)
        font.setPointSizeF(zoomed_point_size(self._base_font.pointSizeF(), self._zoom_percent))
        self.setFont(font)

    def _contains_local_files(self, mime_data: QMimeData) -> bool:
        return bool(self._local_files(mime_data))

    @staticmethod
    def _local_files(mime_data: QMimeData) -> list[Path]:
        return [Path(url.toLocalFile()) for url in mime_data.urls() if url.isLocalFile()]
