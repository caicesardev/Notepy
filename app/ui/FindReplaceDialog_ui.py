# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FindReplaceDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_FindReplaceDialog(object):
    def setupUi(self, FindReplaceDialog):
        if not FindReplaceDialog.objectName():
            FindReplaceDialog.setObjectName(u"FindReplaceDialog")
        FindReplaceDialog.resize(460, 180)
        self.dialog_layout = QGridLayout(FindReplaceDialog)
        self.dialog_layout.setObjectName(u"dialog_layout")
        self.find_label = QLabel(FindReplaceDialog)
        self.find_label.setObjectName(u"find_label")

        self.dialog_layout.addWidget(self.find_label, 0, 0, 1, 1)

        self.find_edit = QLineEdit(FindReplaceDialog)
        self.find_edit.setObjectName(u"find_edit")
        self.find_edit.setClearButtonEnabled(True)

        self.dialog_layout.addWidget(self.find_edit, 0, 1, 1, 1)

        self.find_next_button = QPushButton(FindReplaceDialog)
        self.find_next_button.setObjectName(u"find_next_button")

        self.dialog_layout.addWidget(self.find_next_button, 0, 2, 1, 1)

        self.replace_label = QLabel(FindReplaceDialog)
        self.replace_label.setObjectName(u"replace_label")

        self.dialog_layout.addWidget(self.replace_label, 1, 0, 1, 1)

        self.replace_edit = QLineEdit(FindReplaceDialog)
        self.replace_edit.setObjectName(u"replace_edit")
        self.replace_edit.setClearButtonEnabled(True)

        self.dialog_layout.addWidget(self.replace_edit, 1, 1, 1, 1)

        self.find_previous_button = QPushButton(FindReplaceDialog)
        self.find_previous_button.setObjectName(u"find_previous_button")

        self.dialog_layout.addWidget(self.find_previous_button, 1, 2, 1, 1)

        self.options_group = QGroupBox(FindReplaceDialog)
        self.options_group.setObjectName(u"options_group")
        self.options_layout = QVBoxLayout(self.options_group)
        self.options_layout.setObjectName(u"options_layout")
        self.case_sensitive_check = QCheckBox(self.options_group)
        self.case_sensitive_check.setObjectName(u"case_sensitive_check")

        self.options_layout.addWidget(self.case_sensitive_check)

        self.whole_words_check = QCheckBox(self.options_group)
        self.whole_words_check.setObjectName(u"whole_words_check")

        self.options_layout.addWidget(self.whole_words_check)

        self.wrap_around_check = QCheckBox(self.options_group)
        self.wrap_around_check.setObjectName(u"wrap_around_check")
        self.wrap_around_check.setChecked(True)

        self.options_layout.addWidget(self.wrap_around_check)


        self.dialog_layout.addWidget(self.options_group, 2, 0, 3, 2)

        self.replace_button = QPushButton(FindReplaceDialog)
        self.replace_button.setObjectName(u"replace_button")

        self.dialog_layout.addWidget(self.replace_button, 2, 2, 1, 1)

        self.replace_all_button = QPushButton(FindReplaceDialog)
        self.replace_all_button.setObjectName(u"replace_all_button")

        self.dialog_layout.addWidget(self.replace_all_button, 3, 2, 1, 1)

        self.close_button = QPushButton(FindReplaceDialog)
        self.close_button.setObjectName(u"close_button")

        self.dialog_layout.addWidget(self.close_button, 4, 2, 1, 1)

#if QT_CONFIG(shortcut)
        self.find_label.setBuddy(self.find_edit)
        self.replace_label.setBuddy(self.replace_edit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.find_edit, self.replace_edit)
        QWidget.setTabOrder(self.replace_edit, self.case_sensitive_check)
        QWidget.setTabOrder(self.case_sensitive_check, self.whole_words_check)
        QWidget.setTabOrder(self.whole_words_check, self.wrap_around_check)
        QWidget.setTabOrder(self.wrap_around_check, self.find_next_button)
        QWidget.setTabOrder(self.find_next_button, self.find_previous_button)
        QWidget.setTabOrder(self.find_previous_button, self.replace_button)
        QWidget.setTabOrder(self.replace_button, self.replace_all_button)
        QWidget.setTabOrder(self.replace_all_button, self.close_button)

        self.retranslateUi(FindReplaceDialog)

        self.find_next_button.setDefault(True)


        QMetaObject.connectSlotsByName(FindReplaceDialog)
    # setupUi

    def retranslateUi(self, FindReplaceDialog):
        FindReplaceDialog.setWindowTitle(QCoreApplication.translate("FindReplaceDialog", u"Buscar y reemplazar", None))
        self.find_label.setText(QCoreApplication.translate("FindReplaceDialog", u"&Buscar:", None))
        self.find_next_button.setText(QCoreApplication.translate("FindReplaceDialog", u"Buscar &siguiente", None))
        self.replace_label.setText(QCoreApplication.translate("FindReplaceDialog", u"Reemplazar &por:", None))
        self.find_previous_button.setText(QCoreApplication.translate("FindReplaceDialog", u"Buscar &anterior", None))
        self.options_group.setTitle(QCoreApplication.translate("FindReplaceDialog", u"Opciones", None))
        self.case_sensitive_check.setText(QCoreApplication.translate("FindReplaceDialog", u"&Coincidir may\u00fasculas y min\u00fasculas", None))
        self.whole_words_check.setText(QCoreApplication.translate("FindReplaceDialog", u"Solo palabras &completas", None))
        self.wrap_around_check.setText(QCoreApplication.translate("FindReplaceDialog", u"&Ajuste autom\u00e1tico", None))
        self.replace_button.setText(QCoreApplication.translate("FindReplaceDialog", u"&Reemplazar", None))
        self.replace_all_button.setText(QCoreApplication.translate("FindReplaceDialog", u"Reemplazar &todo", None))
        self.close_button.setText(QCoreApplication.translate("FindReplaceDialog", u"Cerrar", None))
    # retranslateUi

