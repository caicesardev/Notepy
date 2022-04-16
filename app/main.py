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
    QMessageBox
)


__version__ = "1.0.0"


# MainWindow.
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.file_saved = False
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
        self.action_exit.triggered.connect(self.closeEvent)

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

    def on_changes(self):
        if self.path == '':
            self.setWindowTitle("*Sin Título: Notepy")
        else:
            if not self.file_opened:
                self.setWindowTitle(f"*{os.path.basename(self.path)}: Notepy")

    #### File ####

    def new_file(self):
        pass

    def new_window(self):
        subprocess.Popen([sys.executable, "./main.py"])
        os.system('cls' if os.name == 'nt' else 'clear')

    def open_file(self):
        self.path = QFileDialog.getOpenFileName(
            self, "Abrir", "", "Documentos de texto (*.txt);;Todos los archivos (*.*)")
        self.fname = self.path[0]
        if self.path == '':
            return
        try:
            with open(self.fname, 'r') as f:
                content = f.read()
                self.setWindowTitle(f"{os.path.basename(self.fname)}: Notepy")
                self.editor.setPlainText(content)
                self.file_opened = True
        except Exception as e:
            self.file_saved = False
            self.file_opened = False
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
            self.file_saved = False
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
                self.file_saved = True
        except Exception as e:
            self.file_saved = False
            print(e)

    def page_settings(self):
        pass

    def print_file(self):
        pass

    def closeEvent(self, event):
        if not self.file_saved:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            if self.path == "":
                msg.setText("¿Quieres guardar los cambiso de Sin título?")
            else:
                msg.setText(f"¿Quieres guardar los cambios de {self.path}?")
            msg.setInformativeText("This is additional information")
            msg.setWindowTitle("MessageBox demo")
            msg.setDetailedText("The details are as follows:")
            msg.setStandardButtons(
                QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel)

            if msg == QMessageBox.Save:
                print("Save")
            if msg == QMessageBox.No:
                print("Don't save")
            if msg == QMessageBox.Cancel:
                print("Cancel")

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
        else:
            QTextEdit.wheelEvent(self, event)

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
