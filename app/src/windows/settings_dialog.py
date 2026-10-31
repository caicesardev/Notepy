from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QDialog, QWidget

from src.models.theme import Theme
from src.settings.preferences import Preferences
from ui.SettingsDialog_ui import Ui_SettingsDialog

REGULAR_STYLE = "Regular"


class SettingsDialog(QDialog, Ui_SettingsDialog):
    def __init__(self, preferences: Preferences, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self._preferences = preferences
        self._theme_radios = {
            Theme.LIGHT: self.light_theme_radio,
            Theme.DARK: self.dark_theme_radio,
            Theme.SYSTEM: self.system_theme_radio,
        }
        self._load_preferences()
        self._connect_signals()

    def accept(self) -> None:
        self._preferences.theme = self._selected_theme()
        self._preferences.font = self._selected_font()
        super().accept()

    def _load_preferences(self) -> None:
        self._theme_radios[self._preferences.theme].setChecked(True)
        font = self._preferences.font
        self.family_combo.setCurrentFont(font)
        self._populate_styles(font.family(), QFontDatabase.styleString(font))
        self.size_spin.setValue(round(font.pointSizeF()))
        self._refresh_preview()

    def _connect_signals(self) -> None:
        self.family_combo.currentFontChanged.connect(self._on_family_changed)
        self.style_combo.currentTextChanged.connect(self._refresh_preview)
        self.size_spin.valueChanged.connect(self._refresh_preview)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def _on_family_changed(self, font: QFont) -> None:
        self._populate_styles(font.family(), self.style_combo.currentText())
        self._refresh_preview()

    def _populate_styles(self, family: str, preferred_style: str) -> None:
        styles = QFontDatabase.styles(family) or [REGULAR_STYLE]
        self.style_combo.blockSignals(True)
        self.style_combo.clear()
        self.style_combo.addItems(styles)
        self.style_combo.setCurrentText(preferred_style if preferred_style in styles else self._default_style(styles))
        self.style_combo.blockSignals(False)

    @staticmethod
    def _default_style(styles: list[str]) -> str:
        return REGULAR_STYLE if REGULAR_STYLE in styles else styles[0]

    def _refresh_preview(self) -> None:
        self.preview_label.setFont(self._selected_font())

    def _selected_font(self) -> QFont:
        family = self.family_combo.currentFont().family()
        return QFontDatabase.font(family, self.style_combo.currentText(), self.size_spin.value())

    def _selected_theme(self) -> Theme:
        return next(theme for theme, radio in self._theme_radios.items() if radio.isChecked())
