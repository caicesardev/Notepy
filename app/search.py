import sys
import os

from ui.ui_SearchDialog import Ui_SearchDialog
from PySide6.QtCore import (
    Qt,
    QLibraryInfo,
    QLocale,
    QTranslator,
)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QStyle,
)

__version__ = "1.0.0"


# MainWindow.
class SearchDialog(QDialog, Ui_SearchDialog):
    def __init__(self, parent=None):
        super(SearchDialog, self).__init__(parent)

        self.init_ui()

        self.parent = parent

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

        self.close_button.clicked.connect(self.close)

    def search_string(self):
        # --> use self.editor.find(string) or self.parent.editor.find(string) in this case.
        pass


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
