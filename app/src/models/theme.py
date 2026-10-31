from enum import Enum

from PySide6.QtCore import Qt


class Theme(Enum):
    SYSTEM = ("system", Qt.ColorScheme.Unknown)
    LIGHT = ("light", Qt.ColorScheme.Light)
    DARK = ("dark", Qt.ColorScheme.Dark)

    def __init__(self, key: str, color_scheme: Qt.ColorScheme) -> None:
        self.key = key
        self.color_scheme = color_scheme

    @classmethod
    def from_key(cls, key: str) -> "Theme":
        return next((theme for theme in cls if theme.key == key), cls.SYSTEM)
