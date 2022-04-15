import sys

from ui.ui_Settings import Ui_Dialog
from PySide6.QtCore import (
    QLibraryInfo,
    QLocale,
    QTranslator,
)
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
)

__version__ = "1.0.0"


# MainWindow.
class Settings(QDialog, Ui_Dialog):
    def __init__(self):
        super(Settings, self).__init__()

        self.init_ui()

    # First UI setup.
    def init_ui(self):
        self.setupUi(self)
        self.exec_()


def main():
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load("qtbase_" + QLocale.system().name(),
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    gui = Settings()
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
