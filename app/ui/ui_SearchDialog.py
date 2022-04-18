# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SearchDialoggURqGA.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout)

class Ui_SearchDialog(object):
    def setupUi(self, SearchDialog):
        if not SearchDialog.objectName():
            SearchDialog.setObjectName(u"SearchDialog")
        SearchDialog.resize(485, 120)
        SearchDialog.setMinimumSize(QSize(485, 120))
        SearchDialog.setMaximumSize(QSize(485, 120))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        SearchDialog.setFont(font)
        self.verticalLayout = QVBoxLayout(SearchDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(SearchDialog)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"QFrame#container { border: 1px solid #cccccc; border-radius: 5px; background: #f2f2f2; }")
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_frame = QFrame(self.container)
        self.top_frame.setObjectName(u"top_frame")
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.search_edit = QLineEdit(self.top_frame)
        self.search_edit.setObjectName(u"search_edit")
        self.search_edit.setMinimumSize(QSize(0, 30))
        self.search_edit.setFont(font)
        self.search_edit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.search_edit)

        self.find_next_button = QPushButton(self.top_frame)
        self.find_next_button.setObjectName(u"find_next_button")
        self.find_next_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.find_next_button.setFlat(True)

        self.horizontalLayout.addWidget(self.find_next_button)

        self.find_previous_button = QPushButton(self.top_frame)
        self.find_previous_button.setObjectName(u"find_previous_button")
        self.find_previous_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.find_previous_button.setFlat(True)

        self.horizontalLayout.addWidget(self.find_previous_button)

        self.options_button = QPushButton(self.top_frame)
        self.options_button.setObjectName(u"options_button")
        self.options_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.options_button.setFlat(True)

        self.horizontalLayout.addWidget(self.options_button)

        self.close_button = QPushButton(self.top_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_button.setFlat(True)

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout_2.addWidget(self.top_frame)

        self.bottom_frame = QFrame(self.container)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.replace_edit = QLineEdit(self.bottom_frame)
        self.replace_edit.setObjectName(u"replace_edit")
        self.replace_edit.setMinimumSize(QSize(0, 30))
        self.replace_edit.setFont(font)
        self.replace_edit.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.replace_edit)

        self.replace_button = QPushButton(self.bottom_frame)
        self.replace_button.setObjectName(u"replace_button")
        self.replace_button.setFont(font)
        self.replace_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.replace_button.setStyleSheet(u"QPushButton { padding: 7px; }")

        self.horizontalLayout_2.addWidget(self.replace_button)

        self.replace_all_button = QPushButton(self.bottom_frame)
        self.replace_all_button.setObjectName(u"replace_all_button")
        self.replace_all_button.setFont(font)
        self.replace_all_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.replace_all_button.setStyleSheet(u"QPushButton { padding: 7px; }")

        self.horizontalLayout_2.addWidget(self.replace_all_button)


        self.verticalLayout_2.addWidget(self.bottom_frame)


        self.verticalLayout.addWidget(self.container)


        self.retranslateUi(SearchDialog)

        QMetaObject.connectSlotsByName(SearchDialog)
    # setupUi

    def retranslateUi(self, SearchDialog):
        SearchDialog.setWindowTitle(QCoreApplication.translate("SearchDialog", u"Notepy: Buscar y reemplazar", None))
        self.search_edit.setPlaceholderText(QCoreApplication.translate("SearchDialog", u"Buscar", None))
#if QT_CONFIG(tooltip)
        self.find_next_button.setToolTip(QCoreApplication.translate("SearchDialog", u"Buscar abajo", None))
#endif // QT_CONFIG(tooltip)
        self.find_next_button.setText("")
#if QT_CONFIG(tooltip)
        self.find_previous_button.setToolTip(QCoreApplication.translate("SearchDialog", u"Buscar arriba", None))
#endif // QT_CONFIG(tooltip)
        self.find_previous_button.setText("")
#if QT_CONFIG(tooltip)
        self.options_button.setToolTip(QCoreApplication.translate("SearchDialog", u"M\u00e1s opciones", None))
#endif // QT_CONFIG(tooltip)
        self.options_button.setText("")
#if QT_CONFIG(tooltip)
        self.close_button.setToolTip(QCoreApplication.translate("SearchDialog", u"Salir de Buscar y reemplazar", None))
#endif // QT_CONFIG(tooltip)
        self.close_button.setText("")
        self.replace_edit.setPlaceholderText(QCoreApplication.translate("SearchDialog", u"Reemplazar", None))
        self.replace_button.setText(QCoreApplication.translate("SearchDialog", u"Reemplazar", None))
        self.replace_all_button.setText(QCoreApplication.translate("SearchDialog", u"Reemplazar todo", None))
    # retranslateUi

