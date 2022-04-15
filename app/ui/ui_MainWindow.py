# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowVJlDNW.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(793, 600)
        font = QFont()
        font.setFamilies([u"Roboto"])
        MainWindow.setFont(font)
        self.action_new = QAction(MainWindow)
        self.action_new.setObjectName(u"action_new")
        self.action_new_window = QAction(MainWindow)
        self.action_new_window.setObjectName(u"action_new_window")
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_save_as = QAction(MainWindow)
        self.action_save_as.setObjectName(u"action_save_as")
        self.action_page_settings = QAction(MainWindow)
        self.action_page_settings.setObjectName(u"action_page_settings")
        self.action_print = QAction(MainWindow)
        self.action_print.setObjectName(u"action_print")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_undo = QAction(MainWindow)
        self.action_undo.setObjectName(u"action_undo")
        self.action_cut = QAction(MainWindow)
        self.action_cut.setObjectName(u"action_cut")
        self.action_copy = QAction(MainWindow)
        self.action_copy.setObjectName(u"action_copy")
        self.action_paste = QAction(MainWindow)
        self.action_paste.setObjectName(u"action_paste")
        self.action_delete = QAction(MainWindow)
        self.action_delete.setObjectName(u"action_delete")
        self.action_search = QAction(MainWindow)
        self.action_search.setObjectName(u"action_search")
        self.action_search_next = QAction(MainWindow)
        self.action_search_next.setObjectName(u"action_search_next")
        self.action_search_before = QAction(MainWindow)
        self.action_search_before.setObjectName(u"action_search_before")
        self.action_replace = QAction(MainWindow)
        self.action_replace.setObjectName(u"action_replace")
        self.action_goto = QAction(MainWindow)
        self.action_goto.setObjectName(u"action_goto")
        self.action_select_all = QAction(MainWindow)
        self.action_select_all.setObjectName(u"action_select_all")
        self.action_datetime = QAction(MainWindow)
        self.action_datetime.setObjectName(u"action_datetime")
        self.action_font = QAction(MainWindow)
        self.action_font.setObjectName(u"action_font")
        self.action_zoom_in = QAction(MainWindow)
        self.action_zoom_in.setObjectName(u"action_zoom_in")
        self.action_zoom_out = QAction(MainWindow)
        self.action_zoom_out.setObjectName(u"action_zoom_out")
        self.action_restore_zoom = QAction(MainWindow)
        self.action_restore_zoom.setObjectName(u"action_restore_zoom")
        self.action_status_bar = QAction(MainWindow)
        self.action_status_bar.setObjectName(u"action_status_bar")
        self.action_status_bar.setCheckable(True)
        self.action_linebreak = QAction(MainWindow)
        self.action_linebreak.setObjectName(u"action_linebreak")
        self.action_linebreak.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 793, 21))
        self.file = QMenu(self.menubar)
        self.file.setObjectName(u"file")
        self.edit = QMenu(self.menubar)
        self.edit.setObjectName(u"edit")
        self.view = QMenu(self.menubar)
        self.view.setObjectName(u"view")
        self.menuZoom = QMenu(self.view)
        self.menuZoom.setObjectName(u"menuZoom")
        self.settings = QMenu(self.menubar)
        self.settings.setObjectName(u"settings")
        MainWindow.setMenuBar(self.menubar)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.edit.menuAction())
        self.menubar.addAction(self.view.menuAction())
        self.menubar.addAction(self.settings.menuAction())
        self.file.addAction(self.action_new)
        self.file.addAction(self.action_new_window)
        self.file.addAction(self.action_open)
        self.file.addAction(self.action_save)
        self.file.addAction(self.action_save_as)
        self.file.addSeparator()
        self.file.addAction(self.action_page_settings)
        self.file.addAction(self.action_print)
        self.file.addSeparator()
        self.file.addAction(self.action_exit)
        self.edit.addAction(self.action_undo)
        self.edit.addSeparator()
        self.edit.addAction(self.action_cut)
        self.edit.addAction(self.action_copy)
        self.edit.addAction(self.action_paste)
        self.edit.addAction(self.action_delete)
        self.edit.addSeparator()
        self.edit.addAction(self.action_search)
        self.edit.addAction(self.action_search_next)
        self.edit.addAction(self.action_search_before)
        self.edit.addAction(self.action_replace)
        self.edit.addAction(self.action_goto)
        self.edit.addSeparator()
        self.edit.addAction(self.action_select_all)
        self.edit.addAction(self.action_datetime)
        self.edit.addSeparator()
        self.edit.addAction(self.action_font)
        self.view.addAction(self.menuZoom.menuAction())
        self.view.addAction(self.action_status_bar)
        self.view.addAction(self.action_linebreak)
        self.menuZoom.addAction(self.action_zoom_in)
        self.menuZoom.addAction(self.action_zoom_out)
        self.menuZoom.addAction(self.action_restore_zoom)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Notepy", None))
        self.action_new.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
#if QT_CONFIG(shortcut)
        self.action_new.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_new_window.setText(QCoreApplication.translate("MainWindow", u"Nueva ventana", None))
#if QT_CONFIG(shortcut)
        self.action_new_window.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.action_open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.action_save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_save_as.setText(QCoreApplication.translate("MainWindow", u"Guardar como", None))
#if QT_CONFIG(shortcut)
        self.action_save_as.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_page_settings.setText(QCoreApplication.translate("MainWindow", u"Configurar p\u00e1gina", None))
        self.action_print.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
#if QT_CONFIG(shortcut)
        self.action_print.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.action_undo.setText(QCoreApplication.translate("MainWindow", u"Deshacer", None))
#if QT_CONFIG(shortcut)
        self.action_undo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.action_cut.setText(QCoreApplication.translate("MainWindow", u"Cortar", None))
#if QT_CONFIG(shortcut)
        self.action_cut.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.action_copy.setText(QCoreApplication.translate("MainWindow", u"Copiar", None))
#if QT_CONFIG(shortcut)
        self.action_copy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.action_paste.setText(QCoreApplication.translate("MainWindow", u"Pegar", None))
#if QT_CONFIG(shortcut)
        self.action_paste.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.action_delete.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
#if QT_CONFIG(shortcut)
        self.action_delete.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.action_search.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
#if QT_CONFIG(shortcut)
        self.action_search.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.action_search_next.setText(QCoreApplication.translate("MainWindow", u"Buscar siguiente", None))
#if QT_CONFIG(shortcut)
        self.action_search_next.setShortcut(QCoreApplication.translate("MainWindow", u"F3", None))
#endif // QT_CONFIG(shortcut)
        self.action_search_before.setText(QCoreApplication.translate("MainWindow", u"Buscar anterior", None))
#if QT_CONFIG(shortcut)
        self.action_search_before.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+F3", None))
#endif // QT_CONFIG(shortcut)
        self.action_replace.setText(QCoreApplication.translate("MainWindow", u"Reemplazar", None))
#if QT_CONFIG(shortcut)
        self.action_replace.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.action_goto.setText(QCoreApplication.translate("MainWindow", u"Ir a", None))
#if QT_CONFIG(shortcut)
        self.action_goto.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.action_select_all.setText(QCoreApplication.translate("MainWindow", u"Seleccionar todo", None))
#if QT_CONFIG(shortcut)
        self.action_select_all.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.action_datetime.setText(QCoreApplication.translate("MainWindow", u"Fecha y hora", None))
#if QT_CONFIG(shortcut)
        self.action_datetime.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.action_font.setText(QCoreApplication.translate("MainWindow", u"Fuente", None))
        self.action_zoom_in.setText(QCoreApplication.translate("MainWindow", u"Acercar", None))
        self.action_zoom_out.setText(QCoreApplication.translate("MainWindow", u"Alejar", None))
        self.action_restore_zoom.setText(QCoreApplication.translate("MainWindow", u"Restaurar zoom predeterminado", None))
#if QT_CONFIG(shortcut)
        self.action_restore_zoom.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+0", None))
#endif // QT_CONFIG(shortcut)
        self.action_status_bar.setText(QCoreApplication.translate("MainWindow", u"Barra de estado", None))
        self.action_linebreak.setText(QCoreApplication.translate("MainWindow", u"Ajuste de l\u00ednea", None))
        self.file.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.edit.setTitle(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.view.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.menuZoom.setTitle(QCoreApplication.translate("MainWindow", u"Zoom", None))
        self.settings.setTitle(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
    # retranslateUi

