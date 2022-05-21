import sys

from ui.ui_GotoDialog import Ui_GotoDialog
from PySide6.QtCore import (
    Qt,
    QLibraryInfo,
    QLocale,
    QTranslator,
)
from PySide6.QtGui import QIntValidator, QTextCursor
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
)

__version__ = "1.0.0"


# MainWindow.
class GotoDialog(QDialog, Ui_GotoDialog):
    def __init__(self, parent=None):
        super(GotoDialog, self).__init__(parent)

        self.init_ui()

        self.parent = parent

    # First UI setup.
    def init_ui(self):
        self.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.only_int = QIntValidator()
        self.goto_edit.setValidator(self.only_int)

        self.goto_edit.returnPressed.connect(self.goto_line)
        self.goto_button.clicked.connect(self.goto_line)
        self.cancel_button.clicked.connect(self.close)

    def goto_line(self):
        self.line = self.goto_edit.text()
        self.actual_line = self.parent.editor.textCursor().blockNumber() + 1
        if self.actual_line < int(self.line):
            self.move = int(self.line) - self.actual_line
            for i in range(int(self.move)):
                self.parent.editor.moveCursor(QTextCursor.Down)
        elif self.actual_line > int(self.line):
            self.move = int(self.line) - self.actual_line
            for i in range(int(self.line)):
                self.parent.editor.moveCursor(QTextCursor.Up)
        self.close()


def main():
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load("qtbase_" + QLocale.system().name(),
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    gui = GotoDialog()
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
