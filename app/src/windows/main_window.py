import platform
from datetime import datetime
from functools import partial
from pathlib import Path

import PySide6
from PySide6.QtCore import QStandardPaths, Qt, Signal
from PySide6.QtGui import QCloseEvent, QGuiApplication
from PySide6.QtPrintSupport import QAbstractPrintDialog, QPageSetupDialog, QPrintDialog, QPrinter
from PySide6.QtWidgets import QApplication, QFileDialog, QInputDialog, QMainWindow, QMessageBox, QWidget

from constants import APP_NAME, REPOSITORY_URL, UNTITLED_DOCUMENT_NAME, VERSION
from src.models.file_format import FileFormat
from src.models.search_options import SearchOptions
from src.services.recent_files import add_recent_file, remove_recent_file
from src.services.text_codec import read_text_file, write_text_file
from src.services.text_search import TextSearch
from src.settings.preferences import Preferences
from src.windows.find_replace_dialog import FindReplaceDialog
from src.windows.settings_dialog import SettingsDialog
from ui.MainWindow_ui import Ui_MainWindow

TEXT_FILE_FILTER = "Documentos de texto (*.txt)"
ALL_FILES_FILTER = "Todos los archivos (*)"
FILE_FILTERS = f"{TEXT_FILE_FILTER};;{ALL_FILES_FILTER}"
TEXT_FILE_SUFFIX = ".txt"
DATE_TIME_FORMAT = "%H:%M %d/%m/%Y"
STATUS_MESSAGE_TIMEOUT_MS = 5000
PARAGRAPH_SEPARATOR = " "


class MainWindow(QMainWindow, Ui_MainWindow):
    new_window_requested = Signal(object)
    preferences_changed = Signal()

    def __init__(self, preferences: Preferences, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self._preferences = preferences
        self._file_path: Path | None = None
        self._file_format = FileFormat()
        self._printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        self._text_search = TextSearch(self.editor)
        self._last_search: SearchOptions | None = None
        self._find_dialog = FindReplaceDialog(self)
        self._restore_geometry()
        self.apply_preferences()
        self._connect_file_actions()
        self._connect_edit_actions()
        self._connect_view_actions()
        self._connect_help_actions()
        self._connect_editor()
        self._connect_find_dialog()
        self._initialize_edit_actions()
        self._show_document_state()

    def apply_preferences(self) -> None:
        self.editor.set_base_font(self._preferences.font)
        self.action_word_wrap.setChecked(self._preferences.word_wrap)
        self.editor.set_word_wrap(self._preferences.word_wrap)
        self.action_status_bar.setChecked(self._preferences.status_bar_visible)
        self.status_bar.setVisible(self._preferences.status_bar_visible)

    def open_path(self, path: Path) -> bool:
        try:
            decoded = read_text_file(path)
        except OSError as error:
            self._forget_recent_file(path)
            self._show_error(f"No se pudo abrir «{path}».", error)
            return False
        self.editor.setPlainText(decoded.text)
        self._file_path = path.absolute()
        self._file_format = decoded.file_format
        self._remember_recent_file(self._file_path)
        self._show_document_state()
        return True

    def save(self) -> bool:
        if self._file_path is None:
            return self.save_as()
        return self._write_document(self._file_path)

    def save_as(self) -> bool:
        file_name, selected_filter = QFileDialog.getSaveFileName(
            self, "Guardar como", str(self._suggested_save_path()), FILE_FILTERS
        )
        if not file_name:
            return False
        return self._write_document(with_text_suffix(Path(file_name), selected_filter))

    def closeEvent(self, event: QCloseEvent) -> None:
        if not self._confirm_discard_changes():
            event.ignore()
            return
        self._preferences.window_geometry = self.saveGeometry()
        event.accept()

    @property
    def _document_name(self) -> str:
        return self._file_path.name if self._file_path else UNTITLED_DOCUMENT_NAME

    def _connect_file_actions(self) -> None:
        self.action_new.triggered.connect(self._new_document)
        self.action_new_window.triggered.connect(lambda: self.new_window_requested.emit(None))
        self.action_open.triggered.connect(self._choose_file_to_open)
        self.recent_files_menu.aboutToShow.connect(self._populate_recent_files_menu)
        self.action_save.triggered.connect(self.save)
        self.action_save_as.triggered.connect(self.save_as)
        self.action_page_setup.triggered.connect(self._open_page_setup)
        self.action_print.triggered.connect(self._print_document)
        self.action_settings.triggered.connect(self._open_settings)
        self.action_exit.triggered.connect(self.close)

    def _connect_edit_actions(self) -> None:
        self.action_undo.triggered.connect(self.editor.undo)
        self.action_redo.triggered.connect(self.editor.redo)
        self.action_cut.triggered.connect(self.editor.cut)
        self.action_copy.triggered.connect(self.editor.copy)
        self.action_paste.triggered.connect(self.editor.paste)
        self.action_delete.triggered.connect(self.editor.delete_forward)
        self.action_find.triggered.connect(lambda: self._find_dialog.open_for_find(self._selected_line_text()))
        self.action_find_next.triggered.connect(lambda: self._repeat_last_search(backward=False))
        self.action_find_previous.triggered.connect(lambda: self._repeat_last_search(backward=True))
        self.action_replace.triggered.connect(lambda: self._find_dialog.open_for_replace(self._selected_line_text()))
        self.action_go_to_line.triggered.connect(self._go_to_line)
        self.action_select_all.triggered.connect(self.editor.selectAll)
        self.action_insert_date_time.triggered.connect(self._insert_date_time)
        self.action_font.triggered.connect(self._open_settings)

    def _connect_view_actions(self) -> None:
        self.action_zoom_in.triggered.connect(self.editor.zoom_in)
        self.action_zoom_out.triggered.connect(self.editor.zoom_out)
        self.action_reset_zoom.triggered.connect(self.editor.reset_zoom)
        self.action_status_bar.toggled.connect(self._set_status_bar_visible)
        self.action_word_wrap.toggled.connect(self._set_word_wrap)

    def _connect_help_actions(self) -> None:
        self.action_about.triggered.connect(self._show_about)
        self.action_about_qt.triggered.connect(QApplication.aboutQt)

    def _connect_editor(self) -> None:
        document = self.editor.document()
        document.modificationChanged.connect(self.setWindowModified)
        self.editor.cursorPositionChanged.connect(self._show_cursor_position)
        self.editor.textChanged.connect(self._show_character_count)
        self.editor.zoom_changed.connect(self.status_bar.show_zoom)
        self.editor.files_dropped.connect(self._open_dropped_files)
        self.editor.undoAvailable.connect(self.action_undo.setEnabled)
        self.editor.redoAvailable.connect(self.action_redo.setEnabled)
        for action in (self.action_cut, self.action_copy, self.action_delete):
            self.editor.copyAvailable.connect(action.setEnabled)
        QGuiApplication.clipboard().dataChanged.connect(self._refresh_paste_action)

    def _connect_find_dialog(self) -> None:
        self._find_dialog.find_requested.connect(self._find)
        self._find_dialog.replace_requested.connect(self._replace)
        self._find_dialog.replace_all_requested.connect(self._replace_all)
        self._find_dialog.rejected.connect(self.editor.setFocus)

    def _initialize_edit_actions(self) -> None:
        for action in (self.action_undo, self.action_redo, self.action_cut, self.action_copy, self.action_delete):
            action.setEnabled(False)
        self._refresh_paste_action()

    def _new_document(self) -> None:
        if not self._confirm_discard_changes():
            return
        self.editor.clear()
        self._file_path = None
        self._file_format = FileFormat()
        self._show_document_state()

    def _choose_file_to_open(self) -> None:
        if not self._confirm_discard_changes():
            return
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir", self._dialog_directory(), FILE_FILTERS)
        if file_name:
            self.open_path(Path(file_name))

    def _open_recent_file(self, path: Path) -> None:
        if self._confirm_discard_changes():
            self.open_path(path)

    def _open_dropped_files(self, paths: list[Path]) -> None:
        first_path, *other_paths = paths
        if self._confirm_discard_changes():
            self.open_path(first_path)
        for path in other_paths:
            self.new_window_requested.emit(path)

    def _write_document(self, path: Path) -> bool:
        try:
            write_text_file(path, self.editor.toPlainText(), self._file_format)
        except OSError as error:
            self._show_error(f"No se pudo guardar «{path}».", error)
            return False
        self._file_path = path.absolute()
        self._remember_recent_file(self._file_path)
        self._show_document_state()
        return True

    def _confirm_discard_changes(self) -> bool:
        if not self.editor.document().isModified():
            return True
        message_box = QMessageBox(
            QMessageBox.Icon.Question,
            APP_NAME,
            f"¿Quieres guardar los cambios de {self._document_name}?",
            QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel,
            self,
        )
        message_box.button(QMessageBox.StandardButton.Save).setText("Guardar")
        message_box.button(QMessageBox.StandardButton.Discard).setText("No guardar")
        message_box.button(QMessageBox.StandardButton.Cancel).setText("Cancelar")
        message_box.setDefaultButton(QMessageBox.StandardButton.Save)
        message_box.exec()
        answer = message_box.standardButton(message_box.clickedButton())
        if answer == QMessageBox.StandardButton.Save:
            return self.save()
        return answer == QMessageBox.StandardButton.Discard

    def _show_document_state(self) -> None:
        self.editor.document().setModified(False)
        self.setWindowTitle(f"[*]{self._document_name}: {APP_NAME}")
        self.setWindowModified(False)
        self.status_bar.show_file_format(self._file_format)
        self._show_cursor_position()
        self._show_character_count()

    def _show_cursor_position(self) -> None:
        self.status_bar.show_cursor_position(self.editor.cursor_line, self.editor.cursor_column)

    def _show_character_count(self) -> None:
        self.status_bar.show_character_count(self.editor.character_count)

    def _populate_recent_files_menu(self) -> None:
        self.recent_files_menu.clear()
        recent_files = self._preferences.recent_files
        for position, path in enumerate(recent_files, start=1):
            action = self.recent_files_menu.addAction(f"&{position} {str(path).replace('&', '&&')}")
            action.triggered.connect(partial(self._open_recent_file, path))
        if not recent_files:
            self.recent_files_menu.addAction("Sin archivos recientes").setEnabled(False)
            return
        self.recent_files_menu.addSeparator()
        self.recent_files_menu.addAction("&Borrar lista", self._clear_recent_files)

    def _remember_recent_file(self, path: Path) -> None:
        self._preferences.recent_files = add_recent_file(self._preferences.recent_files, path)

    def _forget_recent_file(self, path: Path) -> None:
        self._preferences.recent_files = remove_recent_file(self._preferences.recent_files, path)

    def _clear_recent_files(self) -> None:
        self._preferences.recent_files = []

    def _open_page_setup(self) -> None:
        QPageSetupDialog(self._printer, self).exec()

    def _print_document(self) -> None:
        dialog = QPrintDialog(self._printer, self)
        if self.editor.textCursor().hasSelection():
            dialog.setOption(QAbstractPrintDialog.PrintDialogOption.PrintSelection)
        if dialog.exec():
            self._printer.setDocName(self._document_name)
            self.editor.print_(self._printer)

    def _find(self, options: SearchOptions, backward: bool) -> None:
        self._last_search = options
        if not self._text_search.find(options, backward):
            self._show_not_found(options.text)

    def _replace(self, options: SearchOptions, replacement: str) -> None:
        self._last_search = options
        if not self._text_search.replace(options, replacement):
            self._show_not_found(options.text)

    def _replace_all(self, options: SearchOptions, replacement: str) -> None:
        self._last_search = options
        replacements = self._text_search.replace_all(options, replacement)
        if replacements == 0:
            self._show_not_found(options.text)
            return
        noun = "reemplazo" if replacements == 1 else "reemplazos"
        self.status_bar.showMessage(f"{replacements} {noun}", STATUS_MESSAGE_TIMEOUT_MS)

    def _repeat_last_search(self, backward: bool) -> None:
        if self._last_search is None:
            self._find_dialog.open_for_find(self._selected_line_text())
            return
        self._find(self._last_search, backward)

    def _show_not_found(self, text: str) -> None:
        parent = self._find_dialog if self._find_dialog.isVisible() else self
        QMessageBox.information(parent, APP_NAME, f"No se encuentra «{text}».")

    def _selected_line_text(self) -> str:
        selected = self.editor.textCursor().selectedText()
        return "" if PARAGRAPH_SEPARATOR in selected else selected

    def _go_to_line(self) -> None:
        line_number, accepted = QInputDialog.getInt(
            self, "Ir a la línea", "Número de línea:", self.editor.cursor_line, 1, self.editor.line_count
        )
        if accepted:
            self.editor.go_to_line(line_number)

    def _insert_date_time(self) -> None:
        self.editor.insertPlainText(datetime.now().strftime(DATE_TIME_FORMAT))

    def _set_status_bar_visible(self, visible: bool) -> None:
        self.status_bar.setVisible(visible)
        self._preferences.status_bar_visible = visible

    def _set_word_wrap(self, enabled: bool) -> None:
        self.editor.set_word_wrap(enabled)
        self._preferences.word_wrap = enabled

    def _refresh_paste_action(self) -> None:
        self.action_paste.setEnabled(self.editor.canPaste())

    def _open_settings(self) -> None:
        if SettingsDialog(self._preferences, self).exec():
            self.preferences_changed.emit()

    def _show_about(self) -> None:
        QMessageBox.about(
            self,
            f"Acerca de {APP_NAME}",
            f"<h3>{APP_NAME} {VERSION}</h3>"
            "<p>Un bloc de notas sencillo para escribir notas y archivos de texto.</p>"
            f"<p>Python {platform.python_version()} | PySide6 {PySide6.__version__}</p>"
            f'<p><a href="{REPOSITORY_URL}">{REPOSITORY_URL}</a></p>',
        )

    def _show_error(self, message: str, error: OSError) -> None:
        QMessageBox.critical(self, APP_NAME, f"{message}\n\n{error.strerror or error}")

    def _restore_geometry(self) -> None:
        geometry = self._preferences.window_geometry
        if geometry is not None:
            self.restoreGeometry(geometry)

    def _dialog_directory(self) -> str:
        return str(self._file_path.parent) if self._file_path else self._documents_directory()

    def _suggested_save_path(self) -> Path:
        if self._file_path:
            return self._file_path
        return Path(self._documents_directory()) / f"{UNTITLED_DOCUMENT_NAME}{TEXT_FILE_SUFFIX}"

    @staticmethod
    def _documents_directory() -> str:
        return QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation)


def with_text_suffix(path: Path, selected_filter: str) -> Path:
    if selected_filter == TEXT_FILE_FILTER and not path.suffix:
        return path.with_suffix(TEXT_FILE_SUFFIX)
    return path
