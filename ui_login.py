# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(532, 506)
        Login.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 60, 151, 141))
        self.label.setStyleSheet(u"background-color:None;")
        self.label.setPixmap(QPixmap(u"imgs/user.png"))
        self.label.setScaledContents(True)
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 140, 381, 321))
        self.frame.setStyleSheet(u"background-color: rgba(0,0,0,0.2)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(100, 230, 181, 41))
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{color: rgb(255, 255, 255); border-radius: 10px; font-size: 16px; background-color:rgb(0, 0, 10);;}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"\n"
"")
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setGeometry(QRect(60, 140, 251, 31))
        self.txt_password.setStyleSheet(u"color:#fff; font-size: 16px;")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 85, 151, 31))
        self.label_2.setStyleSheet(u"color:#fff; font-size: 16px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        QWidget.setTabOrder(self.txt_password, self.btn_login)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.label.setText("")
        self.btn_login.setText(QCoreApplication.translate("Login", u"LOGIN", None))
        self.txt_password.setText("")
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Digite sua senha", None))
    # retranslateUi

