from pathlib import Path

from PySide6.QtCore import QByteArray, QSettings
from PySide6.QtGui import QFont

from constants import APP_NAME
from src.models.theme import Theme

DEFAULT_FONT_FAMILY = "Consolas"
DEFAULT_FONT_POINT_SIZE = 11

THEME_KEY = "appearance/theme"
FONT_KEY = "editor/font"
WORD_WRAP_KEY = "editor/word_wrap"
STATUS_BAR_VISIBLE_KEY = "window/status_bar_visible"
WINDOW_GEOMETRY_KEY = "window/geometry"
RECENT_FILES_KEY = "files/recent"


class Preferences:
    def __init__(self, settings: QSettings | None = None) -> None:
        self._settings = settings or QSettings(APP_NAME, "Preferences")

    @property
    def theme(self) -> Theme:
        return Theme.from_key(str(self._settings.value(THEME_KEY, Theme.SYSTEM.key)))

    @theme.setter
    def theme(self, theme: Theme) -> None:
        self._settings.setValue(THEME_KEY, theme.key)

    @property
    def font(self) -> QFont:
        font = QFont(DEFAULT_FONT_FAMILY, DEFAULT_FONT_POINT_SIZE)
        stored = str(self._settings.value(FONT_KEY, "") or "")
        if stored:
            font.fromString(stored)
        return font

    @font.setter
    def font(self, font: QFont) -> None:
        self._settings.setValue(FONT_KEY, font.toString())

    @property
    def word_wrap(self) -> bool:
        return bool(self._settings.value(WORD_WRAP_KEY, True, type=bool))

    @word_wrap.setter
    def word_wrap(self, enabled: bool) -> None:
        self._settings.setValue(WORD_WRAP_KEY, enabled)

    @property
    def status_bar_visible(self) -> bool:
        return bool(self._settings.value(STATUS_BAR_VISIBLE_KEY, True, type=bool))

    @status_bar_visible.setter
    def status_bar_visible(self, visible: bool) -> None:
        self._settings.setValue(STATUS_BAR_VISIBLE_KEY, visible)

    @property
    def window_geometry(self) -> QByteArray | None:
        geometry = self._settings.value(WINDOW_GEOMETRY_KEY)
        return geometry if isinstance(geometry, QByteArray) else None

    @window_geometry.setter
    def window_geometry(self, geometry: QByteArray) -> None:
        self._settings.setValue(WINDOW_GEOMETRY_KEY, geometry)

    @property
    def recent_files(self) -> list[Path]:
        stored = self._settings.value(RECENT_FILES_KEY, [], type=list) or []
        return [Path(path) for path in stored]

    @recent_files.setter
    def recent_files(self, paths: list[Path]) -> None:
        self._settings.setValue(RECENT_FILES_KEY, [str(path) for path in paths])
