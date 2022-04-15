# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingswLFoLF.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
    QDialogButtonBox, QFontComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QRadioButton, QSizePolicy,
    QVBoxLayout)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(420, 285)
        Dialog.setMinimumSize(QSize(420, 285))
        Dialog.setMaximumSize(QSize(420, 285))
        Dialog.setStyleSheet(u"QDialog { background: white; }")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(Dialog)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 120))

        self.verticalLayout.addWidget(self.title)

        self.theme_group_box = QGroupBox(Dialog)
        self.theme_group_box.setObjectName(u"theme_group_box")
        self.theme_group_box.setMaximumSize(QSize(16777215, 70))
        self.theme_group_box.setStyleSheet(u"b")
        self.horizontalLayout = QHBoxLayout(self.theme_group_box)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.light_radio_button = QRadioButton(self.theme_group_box)
        self.light_radio_button.setObjectName(u"light_radio_button")
        self.light_radio_button.setChecked(True)

        self.horizontalLayout.addWidget(self.light_radio_button)

        self.dark_radio_button = QRadioButton(self.theme_group_box)
        self.dark_radio_button.setObjectName(u"dark_radio_button")

        self.horizontalLayout.addWidget(self.dark_radio_button)

        self.system_radio_button = QRadioButton(self.theme_group_box)
        self.system_radio_button.setObjectName(u"system_radio_button")

        self.horizontalLayout.addWidget(self.system_radio_button)


        self.verticalLayout.addWidget(self.theme_group_box)

        self.font_group_box = QGroupBox(Dialog)
        self.font_group_box.setObjectName(u"font_group_box")
        self.formLayout = QFormLayout(self.font_group_box)
        self.formLayout.setObjectName(u"formLayout")
        self.family_label = QLabel(self.font_group_box)
        self.family_label.setObjectName(u"family_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.family_label)

        self.family_combo_box = QFontComboBox(self.font_group_box)
        self.family_combo_box.setObjectName(u"family_combo_box")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.family_combo_box)

        self.style_label = QLabel(self.font_group_box)
        self.style_label.setObjectName(u"style_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.style_label)

        self.style_combo_box = QComboBox(self.font_group_box)
        self.style_combo_box.addItem("")
        self.style_combo_box.setObjectName(u"style_combo_box")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.style_combo_box)

        self.size_label = QLabel(self.font_group_box)
        self.size_label.setObjectName(u"size_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.size_label)

        self.size_combo_box = QComboBox(self.font_group_box)
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.addItem("")
        self.size_combo_box.setObjectName(u"size_combo_box")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.size_combo_box)


        self.verticalLayout.addWidget(self.font_group_box)

        self.button_box = QDialogButtonBox(Dialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.button_box)


        self.retranslateUi(Dialog)
        self.button_box.accepted.connect(Dialog.accept)
        self.button_box.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Configuraci\u00f3n", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700; color:#000000;\">Configuraci\u00f3n</span></p></body></html>", None))
        self.theme_group_box.setTitle(QCoreApplication.translate("Dialog", u"Tema de la aplicaci\u00f3n", None))
        self.light_radio_button.setText(QCoreApplication.translate("Dialog", u"Claro", None))
        self.dark_radio_button.setText(QCoreApplication.translate("Dialog", u"Oscuro", None))
        self.system_radio_button.setText(QCoreApplication.translate("Dialog", u"Usar la configuraci\u00f3n del sistema", None))
        self.font_group_box.setTitle(QCoreApplication.translate("Dialog", u"Fuente", None))
        self.family_label.setText(QCoreApplication.translate("Dialog", u"Familia", None))
        self.style_label.setText(QCoreApplication.translate("Dialog", u"Estilo", None))
        self.style_combo_box.setItemText(0, QCoreApplication.translate("Dialog", u"Normal", None))

        self.size_label.setText(QCoreApplication.translate("Dialog", u"Tama\u00f1o", None))
        self.size_combo_box.setItemText(0, QCoreApplication.translate("Dialog", u"8", None))
        self.size_combo_box.setItemText(1, QCoreApplication.translate("Dialog", u"9", None))
        self.size_combo_box.setItemText(2, QCoreApplication.translate("Dialog", u"10", None))
        self.size_combo_box.setItemText(3, QCoreApplication.translate("Dialog", u"11", None))
        self.size_combo_box.setItemText(4, QCoreApplication.translate("Dialog", u"12", None))
        self.size_combo_box.setItemText(5, QCoreApplication.translate("Dialog", u"14", None))
        self.size_combo_box.setItemText(6, QCoreApplication.translate("Dialog", u"16", None))
        self.size_combo_box.setItemText(7, QCoreApplication.translate("Dialog", u"18", None))
        self.size_combo_box.setItemText(8, QCoreApplication.translate("Dialog", u"20", None))
        self.size_combo_box.setItemText(9, QCoreApplication.translate("Dialog", u"22", None))
        self.size_combo_box.setItemText(10, QCoreApplication.translate("Dialog", u"24", None))
        self.size_combo_box.setItemText(11, QCoreApplication.translate("Dialog", u"26", None))
        self.size_combo_box.setItemText(12, QCoreApplication.translate("Dialog", u"28", None))
        self.size_combo_box.setItemText(13, QCoreApplication.translate("Dialog", u"36", None))
        self.size_combo_box.setItemText(14, QCoreApplication.translate("Dialog", u"48", None))
        self.size_combo_box.setItemText(15, QCoreApplication.translate("Dialog", u"72", None))

    # retranslateUi

