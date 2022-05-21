import sys

from ui.ui_Settings import Ui_SettingsDialog
from PySide6.QtCore import (
    QLibraryInfo,
    QLocale,
    QTranslator,
    QSettings,
)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
)

__version__ = "1.0.0"


# MainWindow.
class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)

        self.parent = parent

        self.init_ui()

    # First UI setup.

    def init_ui(self):
        self.setupUi(self)

        self.get_settings()
        self.set_settings()

        self.accept_button.clicked.connect(self.save_settings)
        self.cancel_button.clicked.connect(self.close)

        self.exec_()

    def get_settings(self):
        self.app_settings = QSettings("Notepy", "AppSettings")

    def set_settings(self):
        if self.app_settings.value("light-theme") == "true":
            self.light_radio_button.setChecked(True)
        elif self.app_settings.value("dark-theme") == "true":
            self.dark_radio_button.setChecked(True)
        else:
            self.system_radio_button.setChecked(True)

        self.family_combo_box.setCurrentFont(
            self.app_settings.value("font-family", "Segoe UI"))
        self.style_combo_box.setCurrentText(
            self.app_settings.value("style", "Normal"))
        self.size_combo_box.setCurrentText(
            self.app_settings.value("font-size", "12"))

    def save_settings(self):
        self.app_settings.setValue(
            "light-theme", self.light_radio_button.isChecked())
        self.app_settings.setValue(
            "dark-theme", self.dark_radio_button.isChecked())
        self.app_settings.setValue(
            "sys-theme", self.system_radio_button.isChecked())
        self.app_settings.setValue(
            "font-family", self.family_combo_box.currentText())
        self.app_settings.setValue(
            "style", self.style_combo_box.currentText())
        self.app_settings.setValue(
            "font-size", self.size_combo_box.currentText())
        self.apply_settings()
        self.close()

    def apply_settings(self):
        self.font = QFont()
        self.font.setFamily(self.app_settings.value("font-family"))
        self.font.setPointSize(int(self.app_settings.value("font-size")))
        self.parent.editor.setFont(self.font)


def main():
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load("qtbase_" + QLocale.system().name(),
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    gui = SettingsDialog()
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
