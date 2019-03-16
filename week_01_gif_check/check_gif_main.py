# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\check_gif_main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_check_gif_window(object):
    def setupUi(self, check_gif_window):
        check_gif_window.setObjectName("check_gif_window")
        check_gif_window.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(check_gif_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 10, 300, 300))
        self.label_1.setObjectName("label_1")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(470, 30, 80, 30))
        self.btn_load.setObjectName("btn_load")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(250, 380, 80, 30))
        self.btn_save.setObjectName("btn_next")
        self.btn_discard = QtWidgets.QPushButton(self.centralwidget)
        self.btn_discard.setGeometry(QtCore.QRect(80, 380, 80, 30))
        self.btn_discard.setObjectName("btn_before")
        check_gif_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(check_gif_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 18))
        self.menubar.setObjectName("menubar")
        check_gif_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(check_gif_window)
        self.statusbar.setObjectName("statusbar")
        check_gif_window.setStatusBar(self.statusbar)

        self.retranslateUi(check_gif_window)
        QtCore.QMetaObject.connectSlotsByName(check_gif_window)

    def retranslateUi(self, check_gif_window):
        _translate = QtCore.QCoreApplication.translate
        check_gif_window.setWindowTitle(_translate("check_gif_window", "MainWindow"))
        self.label_1.setText(_translate("check_gif_window", "TextLabel"))
        self.btn_load.setText(_translate("check_gif_window", "loading"))
        self.btn_save.setText(_translate("check_gif_window", "Save"))
        self.btn_discard.setText(_translate("check_gif_window", "discard"))