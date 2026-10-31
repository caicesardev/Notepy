from pathlib import Path

from PySide6.QtCore import QPoint

from src.services.theme_manager import apply_theme
from src.settings.preferences import Preferences
from src.windows.main_window import MainWindow

CASCADE_OFFSET = QPoint(30, 30)


class WindowManager:
    def __init__(self, preferences: Preferences) -> None:
        self._preferences = preferences
        self._windows: list[MainWindow] = []

    def open_window(self, path: Path | None = None) -> MainWindow:
        window = MainWindow(self._preferences)
        if self._windows:
            window.move(self._windows[-1].pos() + CASCADE_OFFSET)
        window.new_window_requested.connect(self.open_window)
        window.preferences_changed.connect(self.apply_preferences)
        window.destroyed.connect(lambda: self._windows.remove(window))
        self._windows.append(window)
        window.show()
        if path is not None:
            window.open_path(path)
        return window

    def apply_preferences(self) -> None:
        apply_theme(self._preferences.theme)
        for window in self._windows:
            window.apply_preferences()
