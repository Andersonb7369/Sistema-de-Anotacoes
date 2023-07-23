# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cad_login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_cad_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(532, 506)
        Login.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 130, 381, 321))
        self.frame.setStyleSheet(u"background-color: rgba(0,0,0,0.2)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
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
        self.btn_cadastar = QPushButton(self.frame)
        self.btn_cadastar.setObjectName(u"btn_cadastar")
        self.btn_cadastar.setGeometry(QRect(110, 240, 151, 41))
        self.btn_cadastar.setStyleSheet(u"QPushButton{color: rgb(255, 255, 255); border-radius: 10px; font-size: 16px; background-color:rgb(0, 0, 10);;}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}")
        self.txt_password2 = QLineEdit(self.frame)
        self.txt_password2.setObjectName(u"txt_password2")
        self.txt_password2.setGeometry(QRect(60, 180, 251, 31))
        self.txt_password2.setStyleSheet(u"color:#fff; font-size: 16px;")
        self.txt_password2.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhSensitiveData)
        self.txt_password2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 40, 151, 141))
        self.label.setStyleSheet(u"background-color:None;")
        self.label.setPixmap(QPixmap(u"../final_programa/imgs/user.png"))
        self.label.setScaledContents(True)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.txt_password.setText("")
        self.txt_password.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"cadastre uma senha", None))
        self.btn_cadastar.setText(QCoreApplication.translate("Login", u"cadastrar", None))
        self.txt_password2.setPlaceholderText(QCoreApplication.translate("Login", u"repita a senha", None))
        self.label.setText("")
    # retranslateUi

