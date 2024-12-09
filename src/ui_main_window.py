# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)
from widgets import DragDropLineEdit

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(359, 272)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        # self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        # self.formLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        # self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        # self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        # self.formLayout.setVerticalSpacing(9)
        # self.formLayout.setContentsMargins(9, 9, 12, 9)
        # self.formLayout.setSpacing(16)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.rename_folder_path = DragDropLineEdit(self.groupBox)
        self.rename_folder_path.setObjectName(u"rename_folder_path")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.rename_folder_path)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.series_name = QLineEdit(self.groupBox)
        self.series_name.setObjectName(u"series_name")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.series_name)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.re_label = QLabel(self.groupBox)
        self.re_label.setObjectName(u"re_label")
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.re_label)

        self.season = QLineEdit(self.groupBox)
        self.season.setObjectName(u"season")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.season)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.year = QLineEdit(self.groupBox)
        self.year.setObjectName(u"year")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.year)

        self.re = QLineEdit(self.groupBox)
        self.re.setObjectName(u"year")
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.re)

        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.video_rename_button = QPushButton(self.tab)
        self.video_rename_button.setObjectName(u"video_rename_button")

        self.horizontalLayout_2.addWidget(self.video_rename_button)

        self.anime_rename_button = QPushButton(self.tab)
        self.anime_rename_button.setObjectName(u"anime_rename_button")

        self.horizontalLayout_2.addWidget(self.anime_rename_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab, "")
        
        ## 页面2布局
        # 添加QWidget组件
        self.aria2_tab = QWidget()
        self.tabWidget.addTab(self.aria2_tab, "Aria2")
        # 添加垂直布局
        self.aria2_tab_layout = QVBoxLayout(self.aria2_tab)
        # 添加aria2关键字输入框
        self.aria2_keyword = QLineEdit(self.aria2_tab)
        self.aria2_tab_layout.addWidget(self.aria2_keyword)
        # 添加aria2按钮
        self.aria2_button = QPushButton("Aria2批量删除")
        self.aria2_tab_layout.addWidget(self.aria2_button)
        # 将tabWidget添加到水平布局
        self.horizontalLayout.addWidget(self.tabWidget)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 359, 21))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u5de5\u5177", None))
        self.groupBox.setTitle(QCoreApplication.translate("mainWindow", u"\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u6587\u4ef6\u5939", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"\u5267\u540d", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"\u5b63\u6570", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"\u5e74\u4efd", None))
        self.re_label.setText(QCoreApplication.translate("mainWindow", "正则表达式", None))
        self.video_rename_button.setText(QCoreApplication.translate("mainWindow", u"\u5267\u96c6\u91cd\u547d\u540d", None))
        self.anime_rename_button.setText(QCoreApplication.translate("mainWindow", u"\u52a8\u6f2b\u91cd\u547d\u540d", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("mainWindow", u"\u89c6\u9891\u6279\u91cf\u91cd\u547d\u540d", None))
    # retranslateUi

