import sys
import os

from ui.ui_SearchDialog import Ui_SearchDialog
from PySide6.QtCore import (
    Qt,
    QLibraryInfo,
    QLocale,
    QTranslator,
)
from PySide6.QtGui import QIcon, QTextDocument
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QStyle,
    QMenu,
    QMessageBox,
)

__version__ = "1.0.0"


# MainWindow.
class SearchDialog(QDialog, Ui_SearchDialog):
    def __init__(self, parent=None):
        super(SearchDialog, self).__init__(parent)

        self.init_ui()

        self.parent = parent
        self.srch_string = ""

    # First UI setup.
    def init_ui(self):
        self.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.find_next_icon = self.style().standardIcon(
            QStyle.SP_TitleBarUnshadeButton)
        self.find_previous_icon = self.style().standardIcon(
            QStyle.SP_TitleBarShadeButton)
        self.options_icon = self.style().standardIcon(
            QStyle.SP_MediaStop)
        if os.name == 'nt':
            self.close_icon = self.style().standardIcon(
                QStyle.SP_TitleBarCloseButton)
        else:
            self.close_icon = self.style().standardIcon(
                QStyle.SP_DialogCancelButton)
        self.find_next_button.setIcon(QIcon(self.find_next_icon))
        self.find_previous_button.setIcon(QIcon(self.find_previous_icon))
        self.options_button.setIcon(QIcon(self.options_icon))
        self.close_button.setIcon(QIcon(self.close_icon))

        self.find_next_button.clicked.connect(self.search_string_forward)
        self.find_previous_button.clicked.connect(self.search_string_backward)
        self.close_button.clicked.connect(self.close)

        menu = QMenu(self)
        self.case_sensitive_action = menu.addAction(
            "Coincidir mayúsculas y minúsculas")
        self.automatic_adjustement_action = menu.addAction("Ajuste automático")
        self.case_sensitive_action.setCheckable(True)
        self.automatic_adjustement_action.setCheckable(True)
        self.automatic_adjustement_action.setChecked(True)
        self.options_button.setMenu(menu)

    def search_string_forward(self):
        if not self.case_sensitive_action.isChecked():
            self.srch_string = self.search_edit.text()
            string = self.parent.editor.find(
                self.srch_string, QTextDocument.FindWholeWords)
            if self.srch_string != "":
                if not string:
                    QMessageBox.information(
                        self,
                        "Notepy: No se pudo encontrar",
                        f"No se pudo encontrar '{self.srch_string}'")
        else:
            self.search_case_sensitively()

    def search_string_backward(self):
        if not self.case_sensitive_action.isChecked():
            self.srch_string = self.search_edit.text()
            string = self.parent.editor.find(
                self.srch_string, QTextDocument.FindBackward)
            if self.srch_string != "":
                if not string:
                    QMessageBox.information(
                        self,
                        "Notepy: No se pudo encontrar",
                        f"No se pudo encontrar '{self.srch_string}'")
        else:
            self.search_case_sensitively()

    def search_case_sensitively(self):
        print("Case sensitive")
        self.srch_string = self.search_edit.text()
        string = self.parent.editor.find(
            self.srch_string, QTextDocument.FindCaseSensitively)
        if self.srch_string != "":
            if not string:
                QMessageBox.information(
                    self,
                    "Notepy: No se pudo encontrar",
                    f"No se pudo encontrar '{self.srch_string}'")


def main():
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load("qtbase_" + QLocale.system().name(),
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    gui = SearchDialog()
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
