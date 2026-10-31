from PySide6.QtGui import QGuiApplication

from src.models.theme import Theme


def apply_theme(theme: Theme) -> None:
    style_hints = QGuiApplication.styleHints()
    if theme is Theme.SYSTEM:
        style_hints.unsetColorScheme()
    else:
        style_hints.setColorScheme(theme.color_scheme)
