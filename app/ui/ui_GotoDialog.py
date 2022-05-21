# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GotoDialogdMKYNz.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout)

class Ui_GotoDialog(object):
    def setupUi(self, GotoDialog):
        if not GotoDialog.objectName():
            GotoDialog.setObjectName(u"GotoDialog")
        GotoDialog.resize(485, 140)
        GotoDialog.setMinimumSize(QSize(485, 140))
        GotoDialog.setMaximumSize(QSize(485, 141))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        GotoDialog.setFont(font)
        self.verticalLayout = QVBoxLayout(GotoDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(GotoDialog)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"QFrame#container { border: 1px solid #cccccc; border-radius: 5px; background: #f2f2f2; }")
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_frame = QFrame(self.container)
        self.top_frame.setObjectName(u"top_frame")
        self.verticalLayout_3 = QVBoxLayout(self.top_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.goto_edit = QLineEdit(self.top_frame)
        self.goto_edit.setObjectName(u"goto_edit")
        self.goto_edit.setMinimumSize(QSize(0, 30))
        self.goto_edit.setFont(font)
        self.goto_edit.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.goto_edit)


        self.verticalLayout_2.addWidget(self.top_frame)

        self.bottom_frame = QFrame(self.container)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.goto_button = QPushButton(self.bottom_frame)
        self.goto_button.setObjectName(u"goto_button")
        self.goto_button.setFont(font)
        self.goto_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.goto_button.setStyleSheet(u"QPushButton { padding: 7px; }")

        self.horizontalLayout_2.addWidget(self.goto_button)

        self.cancel_button = QPushButton(self.bottom_frame)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setFont(font)
        self.cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_button.setStyleSheet(u"QPushButton { padding: 7px; }")

        self.horizontalLayout_2.addWidget(self.cancel_button)


        self.verticalLayout_2.addWidget(self.bottom_frame)


        self.verticalLayout.addWidget(self.container)


        self.retranslateUi(GotoDialog)

        QMetaObject.connectSlotsByName(GotoDialog)
    # setupUi

    def retranslateUi(self, GotoDialog):
        GotoDialog.setWindowTitle(QCoreApplication.translate("GotoDialog", u"Notepy: Ir a la l\u00ednea", None))
        self.label.setText(QCoreApplication.translate("GotoDialog", u"N\u00famero de l\u00ednea", None))
        self.goto_edit.setPlaceholderText(QCoreApplication.translate("GotoDialog", u"1234", None))
        self.goto_button.setText(QCoreApplication.translate("GotoDialog", u"Ir a", None))
        self.cancel_button.setText(QCoreApplication.translate("GotoDialog", u"Cancelar", None))
    # retranslateUi

