from PySide6.QtWidgets import QLabel, QStatusBar, QWidget

from src.models.file_format import FileFormat
from src.services.zoom import DEFAULT_ZOOM_PERCENT

SECTION_STYLE = "QLabel { padding: 0 12px; }"


class DocumentStatusBar(QStatusBar):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._position_label = self._add_section()
        self._characters_label = self._add_section()
        self._zoom_label = self._add_section()
        self._line_ending_label = self._add_section()
        self._encoding_label = self._add_section()
        self.show_cursor_position(1, 1)
        self.show_character_count(0)
        self.show_zoom(DEFAULT_ZOOM_PERCENT)
        self.show_file_format(FileFormat())

    def show_cursor_position(self, line: int, column: int) -> None:
        self._position_label.setText(f"Lín. {line}, col. {column}")

    def show_character_count(self, count: int) -> None:
        noun = "carácter" if count == 1 else "caracteres"
        self._characters_label.setText(f"{count:,} {noun}".replace(",", "."))

    def show_zoom(self, percent: int) -> None:
        self._zoom_label.setText(f"{percent}%")

    def show_file_format(self, file_format: FileFormat) -> None:
        self._line_ending_label.setText(file_format.line_ending.label)
        self._encoding_label.setText(file_format.encoding.label)

    def _add_section(self) -> QLabel:
        label = QLabel(self)
        label.setStyleSheet(SECTION_STYLE)
        self.addPermanentWidget(label)
        return label
