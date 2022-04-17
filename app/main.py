import sys
import os
import subprocess

from ui.ui_MainWindow import Ui_MainWindow
from settings import Settings
from PySide6.QtGui import QKeySequence
from PySide6.QtCore import (
    Qt,
    QLibraryInfo,
    QLocale,
    QTranslator,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QFileDialog,
    QMessageBox,
    QLabel,
    QWidget,
)
from PySide6.QtPrintSupport import QPrinter, QPrintDialog, QPageSetupDialog


__version__ = "1.0.0"


# MainWindow.
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.file_saved = True  # For the default file.
        self.file_opened = False
        self.path = ''

        self.init_ui()

        self.setWindowTitle("Sin título: Notepy")

    # First UI setup.
    def init_ui(self):
        self.setupUi(self)

        self.zoom_in_sct = QKeySequence("Ctrl++")
        self.zoom_out_sct = QKeySequence("Ctrl+-")
        self.action_zoom_in.setShortcut(self.zoom_in_sct)
        self.action_zoom_out.setShortcut(self.zoom_out_sct)

        self.action_new.triggered.connect(self.new_file)
        self.action_new_window.triggered.connect(self.new_window)
        self.action_open.triggered.connect(self.open_file)
        self.action_save.triggered.connect(self.save)
        self.action_save_as.triggered.connect(self.save_as)
        self.action_page_settings.triggered.connect(self.page_settings)
        self.action_print.triggered.connect(self.print_file)
        self.action_exit.triggered.connect(self.close)

        self.action_search.triggered.connect(self.find)
        self.action_find_next.triggered.connect(self.find_next)
        self.action_find_previous.triggered.connect(self.find_previous)
        self.action_replace.triggered.connect(self.replace)
        self.action_goto.triggered.connect(self.goto)
        self.action_datetime.triggered.connect(self.insert_datetime)
        self.action_font.triggered.connect(Settings)

        self.action_zoom_in.triggered.connect(self.zoom_in)
        self.action_zoom_out.triggered.connect(self.zoom_out)
        self.action_restore_zoom.triggered.connect(self.restore_zoom)
        self.action_status_bar.triggered.connect(self.handle_status_bar)
        self.action_word_wrap.triggered.connect(self.handle_word_wrap)

        self.action_settings.triggered.connect(Settings)
        self.action_about_qt.triggered.connect(QApplication.aboutQt)

        self.editor.textChanged.connect(self.on_changes)

        self.encoding_label = QLabel("UTF-8")
        self.os_label = QLabel("Windows (CLRF)")
        # print(repr(f.newlines)) --> To detect if newlines are from windwos \r\f or Unix
        self.zoom_percent = QLabel("100%")
        self.cur_location = QLabel("Ln 1, Col 1")

        self.separator = QWidget()
        self.separator.setFixedWidth(50)
        self.separator.setStyleSheet("border-left: 1px solid grey")

        self.separator2 = QWidget()
        self.separator2.setFixedWidth(50)
        self.separator2.setStyleSheet("border-left: 1px solid grey")

        self.separator3 = QWidget()
        self.separator3.setFixedWidth(50)
        self.separator3.setStyleSheet("border-left: 1px solid grey")

        self.status_bar.addPermanentWidget(self.cur_location)
        self.status_bar.addPermanentWidget(self.separator)
        self.status_bar.addPermanentWidget(self.zoom_percent)
        self.status_bar.addPermanentWidget(self.separator2)
        self.status_bar.addPermanentWidget(self.os_label)
        self.status_bar.addPermanentWidget(self.separator3)
        self.status_bar.addPermanentWidget(self.encoding_label)

    def on_changes(self):
        # Default name.
        if self.path == '':
            # If the user deleted all changes there's nothing to save.
            if self.editor.textCursor().position() == 0:
                self.setWindowTitle("Sin Título: Notepy")
                self.file_saved = True
            else:
                self.setWindowTitle("*Sin Título: Notepy")
                self.file_saved = False
                self.cur_location.setText(
                    f"Ln {self.editor.textCursor().blockNumber() + 1}, Col {self.editor.textCursor().columnNumber() + 1}")
        else:
            # If you have just opened a file dont put the asterisk.
            if self.file_opened:
                # Reset variable
                self.file_opened = False
            else:
                self.setWindowTitle(f"*{os.path.basename(self.path)}: Notepy")
                self.file_saved = False

    #### File ####

    def new_file(self):
        if self.file_saved == False:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            if self.path == "":
                msg.setText("¿Quieres guardar los cambios de Sin título?")
            else:
                msg.setText(f"¿Quieres guardar los cambios de {self.path}?")
            msg.setWindowTitle("Notepy | Guardar cambios")
            msg.setStandardButtons(
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

            ret = msg.exec()

            if ret == QMessageBox.Save:
                self.save()
            if ret == QMessageBox.Discard:
                self.editor.clear()
                self.setWindowTitle("Sin Título: Notepy")
                self.path = ""
                self.file_saved = True
                self.cur_location.setText("Ln 1, Col 1")

            if ret == QMessageBox.Cancel:
                return
        else:
            self.editor.clear()
            self.setWindowTitle("Sin Título: Notepy")
            self.path = ""
            self.file_saved = True
            self.cur_location.setText("Ln 1, Col 1")

    def new_window(self):
        subprocess.Popen([sys.executable, "./main.py"])
        os.system('cls' if os.name == 'nt' else 'clear')

    def open_file(self):
        self.path, _ = QFileDialog.getOpenFileName(
            self, "Abrir", "", "Documentos de texto (*.txt);;Todos los archivos (*.*)")
        if self.path == '':
            return
        try:
            with open(self.path, 'r') as f:
                content = f.read()
                self.file_opened = True
                self.setWindowTitle(f"{os.path.basename(self.path)}: Notepy")
                self.editor.setPlainText(content)
        except Exception as e:
            print(e)

    def save(self):
        if self.path == '':
            self.save_as()
        text = self.editor.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.setWindowTitle(f"{os.path.basename(self.path)}: Notepy")
                self.file_saved = True
        except Exception as e:
            print(e)

    def save_as(self):
        self.path, _ = QFileDialog.getSaveFileName(
            self, "Guardar como", "*.txt", "Documentos de texto (*.txt);;Todos los archivos (*.*)",)
        if self.path == '':
            return
        text = self.editor.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.setWindowTitle(f"{os.path.basename(self.path)}: Notepy")
        except Exception as e:
            print(e)

    def page_settings(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPageSetupDialog(printer)

        if dialog.exec() == QPrintDialog.Accepted:
            return

    def print_file(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer)

        if dialog.exec() == QPrintDialog.Accepted:
            self.editor.print_(printer)

    def closeEvent(self, event):
        if self.file_saved == False:
            self.show_save_message(event)

    def show_save_message(self, event):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        if self.path == "":
            msg.setText("¿Quieres guardar los cambios de Sin título?")
        else:
            msg.setText(f"¿Quieres guardar los cambios de {self.path}?")
        msg.setWindowTitle("Notepy | Guardar cambios")
        msg.setStandardButtons(
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

        ret = msg.exec()

        if ret == QMessageBox.Save:
            self.save()
            event.ignore()
        if ret == QMessageBox.Discard:
            self.close()
        if ret == QMessageBox.Cancel:
            event.ignore()

    #### File ####

    #### Edit ####

    def find(self):
        pass

    def find_next(self):
        pass

    def find_previous(self):
        pass

    def replace(self):
        pass

    def goto(self):
        pass

    def insert_datetime(self):
        pass

    #### Edit ####

    #### View ####

    def zoom_in(self):
        self.editor.zoomIn(+5)

    def zoom_out(self):
        self.editor.zoomOut(+5)

    def zoom(self, delta):
        if delta < 0:
            self.editor.zoomOut(+1)
        elif delta > 0:
            self.editor.zoomIn(+1)

    def wheelEvent(self, event):
        if (event.modifiers() & Qt.ControlModifier):
            self.zoom(event.angleDelta().y())

    def restore_zoom(self):
        pass

    def handle_status_bar(self):
        if not self.action_status_bar.isChecked():
            self.status_bar.hide()
        else:
            self.status_bar.show()

    def handle_word_wrap(self):
        if not self.action_word_wrap.isChecked():
            self.editor.setLineWrapMode(self.editor.NoWrap)
        else:
            self.editor.setLineWrapMode(self.editor.WidgetWidth)

    #### View ####


def main():
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load("qtbase_" + QLocale.system().name(),
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    gui = MainWindow()
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
