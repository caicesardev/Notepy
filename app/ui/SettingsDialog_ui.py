# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFontComboBox, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QRadioButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)
import images_rc

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(440, 360)
        icon = QIcon()
        icon.addFile(u":/icons/notes.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        SettingsDialog.setWindowIcon(icon)
        self.dialog_layout = QVBoxLayout(SettingsDialog)
        self.dialog_layout.setObjectName(u"dialog_layout")
        self.theme_group = QGroupBox(SettingsDialog)
        self.theme_group.setObjectName(u"theme_group")
        self.theme_layout = QHBoxLayout(self.theme_group)
        self.theme_layout.setObjectName(u"theme_layout")
        self.light_theme_radio = QRadioButton(self.theme_group)
        self.light_theme_radio.setObjectName(u"light_theme_radio")

        self.theme_layout.addWidget(self.light_theme_radio)

        self.dark_theme_radio = QRadioButton(self.theme_group)
        self.dark_theme_radio.setObjectName(u"dark_theme_radio")

        self.theme_layout.addWidget(self.dark_theme_radio)

        self.system_theme_radio = QRadioButton(self.theme_group)
        self.system_theme_radio.setObjectName(u"system_theme_radio")
        self.system_theme_radio.setChecked(True)

        self.theme_layout.addWidget(self.system_theme_radio)


        self.dialog_layout.addWidget(self.theme_group)

        self.font_group = QGroupBox(SettingsDialog)
        self.font_group.setObjectName(u"font_group")
        self.font_layout = QFormLayout(self.font_group)
        self.font_layout.setObjectName(u"font_layout")
        self.family_label = QLabel(self.font_group)
        self.family_label.setObjectName(u"family_label")

        self.font_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.family_label)

        self.family_combo = QFontComboBox(self.font_group)
        self.family_combo.setObjectName(u"family_combo")

        self.font_layout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.family_combo)

        self.style_label = QLabel(self.font_group)
        self.style_label.setObjectName(u"style_label")

        self.font_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.style_label)

        self.style_combo = QComboBox(self.font_group)
        self.style_combo.setObjectName(u"style_combo")

        self.font_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.style_combo)

        self.size_label = QLabel(self.font_group)
        self.size_label.setObjectName(u"size_label")

        self.font_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.size_label)

        self.size_spin = QSpinBox(self.font_group)
        self.size_spin.setObjectName(u"size_spin")
        self.size_spin.setMinimum(6)
        self.size_spin.setMaximum(96)
        self.size_spin.setValue(11)

        self.font_layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.size_spin)

        self.preview_label = QLabel(self.font_group)
        self.preview_label.setObjectName(u"preview_label")
        self.preview_label.setMinimumSize(QSize(0, 70))
        self.preview_label.setFrameShape(QFrame.Shape.StyledPanel)
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.font_layout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.preview_label)


        self.dialog_layout.addWidget(self.font_group)

        self.button_box = QDialogButtonBox(SettingsDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.dialog_layout.addWidget(self.button_box)

#if QT_CONFIG(shortcut)
        self.family_label.setBuddy(self.family_combo)
        self.style_label.setBuddy(self.style_combo)
        self.size_label.setBuddy(self.size_spin)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Configuraci\u00f3n", None))
        self.theme_group.setTitle(QCoreApplication.translate("SettingsDialog", u"Tema de la aplicaci\u00f3n", None))
        self.light_theme_radio.setText(QCoreApplication.translate("SettingsDialog", u"&Claro", None))
        self.dark_theme_radio.setText(QCoreApplication.translate("SettingsDialog", u"&Oscuro", None))
        self.system_theme_radio.setText(QCoreApplication.translate("SettingsDialog", u"Usar la configuraci\u00f3n del &sistema", None))
        self.font_group.setTitle(QCoreApplication.translate("SettingsDialog", u"Fuente", None))
        self.family_label.setText(QCoreApplication.translate("SettingsDialog", u"&Familia", None))
        self.style_label.setText(QCoreApplication.translate("SettingsDialog", u"&Estilo", None))
        self.size_label.setText(QCoreApplication.translate("SettingsDialog", u"&Tama\u00f1o", None))
        self.preview_label.setText(QCoreApplication.translate("SettingsDialog", u"AaBbYyZz \u00c1\u00c9\u00cd\u00d3\u00da \u00f1 0123", None))
    # retranslateUi

