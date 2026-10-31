from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QWidget

from src.models.search_options import SearchOptions
from ui.FindReplaceDialog_ui import Ui_FindReplaceDialog

FIND_TITLE = "Buscar"
REPLACE_TITLE = "Reemplazar"


class FindReplaceDialog(QDialog, Ui_FindReplaceDialog):
    find_requested = Signal(object, bool)
    replace_requested = Signal(object, str)
    replace_all_requested = Signal(object, str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._connect_signals()
        self._refresh_buttons()

    @property
    def search_options(self) -> SearchOptions:
        return SearchOptions(
            text=self.find_edit.text(),
            case_sensitive=self.case_sensitive_check.isChecked(),
            whole_words=self.whole_words_check.isChecked(),
            wrap_around=self.wrap_around_check.isChecked(),
        )

    def open_for_find(self, initial_text: str) -> None:
        self._open(initial_text, replace_mode=False)

    def open_for_replace(self, initial_text: str) -> None:
        self._open(initial_text, replace_mode=True)

    def _connect_signals(self) -> None:
        self.find_edit.textChanged.connect(self._refresh_buttons)
        self.find_next_button.clicked.connect(lambda: self.find_requested.emit(self.search_options, False))
        self.find_previous_button.clicked.connect(lambda: self.find_requested.emit(self.search_options, True))
        self.replace_button.clicked.connect(
            lambda: self.replace_requested.emit(self.search_options, self.replace_edit.text())
        )
        self.replace_all_button.clicked.connect(
            lambda: self.replace_all_requested.emit(self.search_options, self.replace_edit.text())
        )
        self.close_button.clicked.connect(self.reject)

    def _open(self, initial_text: str, replace_mode: bool) -> None:
        self._set_replace_mode(replace_mode)
        if initial_text:
            self.find_edit.setText(initial_text)
        self.show()
        self.raise_()
        self.activateWindow()
        self.find_edit.setFocus()
        self.find_edit.selectAll()

    def _set_replace_mode(self, enabled: bool) -> None:
        for widget in (self.replace_label, self.replace_edit, self.replace_button, self.replace_all_button):
            widget.setVisible(enabled)
        self.setWindowTitle(REPLACE_TITLE if enabled else FIND_TITLE)
        self.adjustSize()

    def _refresh_buttons(self) -> None:
        has_search_text = bool(self.find_edit.text())
        for button in (
            self.find_next_button,
            self.find_previous_button,
            self.replace_button,
            self.replace_all_button,
        ):
            button.setEnabled(has_search_text)
