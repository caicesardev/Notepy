import sys
from pathlib import Path

from PySide6.QtCore import QLibraryInfo, QLocale, QTranslator
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from constants import APP_NAME, VERSION
from src.services.theme_manager import apply_theme
from src.settings.preferences import Preferences
from src.windows.window_manager import WindowManager

APP_LOCALE = QLocale(QLocale.Language.Spanish)
APP_ICON = ":/icons/notes.png"


def install_qt_translations(app: QApplication) -> None:
    translator = QTranslator(app)
    translations_path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    if translator.load(APP_LOCALE, "qtbase", "_", translations_path):
        app.installTranslator(translator)


def files_to_open(arguments: list[str]) -> list[Path | None]:
    return [Path(argument) for argument in arguments] or [None]


def main() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(VERSION)
    app.setWindowIcon(QIcon(APP_ICON))
    install_qt_translations(app)

    preferences = Preferences()
    apply_theme(preferences.theme)
    window_manager = WindowManager(preferences)
    for path in files_to_open(app.arguments()[1:]):
        window_manager.open_window(path)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
