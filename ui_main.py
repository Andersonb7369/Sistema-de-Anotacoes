# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 552)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0,10);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 20);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 35))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	 border-radius: 1px;\n"
"	 font-size: 16px;\n"
"	 background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_consultar = QPushButton(self.frame)
        self.btn_consultar.setObjectName(u"btn_consultar")
        self.btn_consultar.setMinimumSize(QSize(0, 33))
        self.btn_consultar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_consultar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	 border-radius: 1px;\n"
"	 font-size: 16px;\n"
"	 background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"")

        self.horizontalLayout.addWidget(self.btn_consultar)

        self.btn_cadastro = QPushButton(self.frame)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setMinimumSize(QSize(0, 33))
        self.btn_cadastro.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	 border-radius: 1px;\n"
"	 font-size: 16px;\n"
"	 background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"")

        self.horizontalLayout.addWidget(self.btn_cadastro)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 33))
        self.btn_contato.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	 border-radius: 1px;\n"
"	 font-size: 16px;\n"
"	 background-color: rgb(0, 80, 121);\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #fff; color:black}\n"
"")

        self.horizontalLayout.addWidget(self.btn_contato)


        self.verticalLayout_2.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout = QVBoxLayout(self.pg_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u" background-color: rgb(0, 80, 121);\n"
"\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.Pages.addWidget(self.pg_home)
        self.pg_consultar = QWidget()
        self.pg_consultar.setObjectName(u"pg_consultar")
        self.pg_consultar.setEnabled(True)
        font = QFont()
        font.setKerning(True)
        self.pg_consultar.setFont(font)
        self.horizontalLayout_3 = QHBoxLayout(self.pg_consultar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.pg_consultar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.txt_search_cm = QLineEdit(self.frame_2)
        self.txt_search_cm.setObjectName(u"txt_search_cm")
        self.txt_search_cm.setMinimumSize(QSize(0, 29))
        self.txt_search_cm.setMaximumSize(QSize(16777215, 24))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.txt_search_cm.setFont(font1)
        self.txt_search_cm.setCursor(QCursor(Qt.PointingHandCursor))
        self.txt_search_cm.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_search_cm.setAlignment(Qt.AlignCenter)
        self.txt_search_cm.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.txt_search_cm)

        self.label_57 = QLabel(self.frame_2)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.label_57)

        self.txt_filter_dc = QLineEdit(self.frame_2)
        self.txt_filter_dc.setObjectName(u"txt_filter_dc")
        self.txt_filter_dc.setMinimumSize(QSize(0, 29))
        self.txt_filter_dc.setMaximumSize(QSize(16777215, 24))
        self.txt_filter_dc.setFont(font1)
        self.txt_filter_dc.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.txt_filter_dc)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.txt_filter_lg = QLineEdit(self.frame_2)
        self.txt_filter_lg.setObjectName(u"txt_filter_lg")
        self.txt_filter_lg.setMinimumSize(QSize(0, 29))
        self.txt_filter_lg.setMaximumSize(QSize(16777215, 24))
        self.txt_filter_lg.setFont(font1)
        self.txt_filter_lg.setCursor(QCursor(Qt.PointingHandCursor))
        self.txt_filter_lg.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_filter_lg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_filter_lg)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tb_geral = QTableView(self.frame_2)
        self.tb_geral.setObjectName(u"tb_geral")

        self.verticalLayout_3.addWidget(self.tb_geral)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")

        self.verticalLayout_3.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_refresh = QPushButton(self.frame_2)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"    border-radius: 10px; \n"
"	font-size: 16px; \n"
"	background-color: #fff;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	 color:black\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_refresh)

        self.btn_excel = QPushButton(self.frame_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"    border-radius: 10px; \n"
"	font-size: 16px; \n"
"	background-color: #fff;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	 color:black\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_excel)

        self.btn_edit = QPushButton(self.frame_2)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"    border-radius: 10px; \n"
"	font-size: 16px; \n"
"	background-color: #fff;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	 color:black\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_edit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.Pages.addWidget(self.pg_consultar)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName(u"label_14")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_14)

        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setPointSize(10)
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(50, -1, -1, -1)
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy2)
        self.txt_nome.setStyleSheet(u"color:rgba(211, 239, 251,1);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155,0.1);\n"
"font-family:Trebuchet MS; \n"
"font-size:21px;")

        self.horizontalLayout_8.addWidget(self.txt_nome)

        self.label_5 = QLabel(self.pg_cadastro)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, -1, -1, -1)
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.txt_comando = QLineEdit(self.pg_cadastro)
        self.txt_comando.setObjectName(u"txt_comando")
        self.txt_comando.setMaximumSize(QSize(16777215, 30))
        self.txt_comando.setStyleSheet(u"color:rgba(211, 239, 251,1);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155,0.1);\n"
"font-family:Trebuchet MS; \n"
"font-size:21px;")

        self.horizontalLayout_7.addWidget(self.txt_comando)

        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(50, -1, -1, -1)
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.txt_descricao = QLineEdit(self.pg_cadastro)
        self.txt_descricao.setObjectName(u"txt_descricao")
        self.txt_descricao.setStyleSheet(u"color:rgba(211, 239, 251,1);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155,0.1);\n"
"font-family:Trebuchet MS; \n"
"font-size:21px;")

        self.horizontalLayout_6.addWidget(self.txt_descricao)

        self.label_16 = QLabel(self.pg_cadastro)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_6.addWidget(self.label_16)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(50, -1, -1, -1)
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.cb_linguagem = QComboBox(self.pg_cadastro)
        self.cb_linguagem.addItem("")
        self.cb_linguagem.addItem("")
        self.cb_linguagem.addItem("")
        self.cb_linguagem.addItem("")
        self.cb_linguagem.addItem("")
        self.cb_linguagem.addItem("")
        self.cb_linguagem.addItem("")
        self.cb_linguagem.addItem("")
        self.cb_linguagem.addItem("")
        self.cb_linguagem.setObjectName(u"cb_linguagem")
        sizePolicy2.setHeightForWidth(self.cb_linguagem.sizePolicy().hasHeightForWidth())
        self.cb_linguagem.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(12)
        self.cb_linguagem.setFont(font4)
        self.cb_linguagem.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.cb_linguagem)

        self.label_17 = QLabel(self.pg_cadastro)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_5.addWidget(self.label_17)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 35))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"    border-radius: 10px; \n"
"	font-size: 16px; \n"
"	background-color: #fff;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	 color:black\n"
"}\n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.verticalLayout_12 = QVBoxLayout(self.pg_contato)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_15 = QLabel(self.pg_contato)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_15)

        self.label_19 = QLabel(self.pg_contato)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_19)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_27 = QLabel(self.pg_contato)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_15.addWidget(self.label_27)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_24 = QLabel(self.pg_contato)
        self.label_24.setObjectName(u"label_24")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy3)

        self.horizontalLayout_12.addWidget(self.label_24)

        self.label_20 = QLabel(self.pg_contato)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_20)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_12)

        self.label_28 = QLabel(self.pg_contato)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_15.addWidget(self.label_28)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_29 = QLabel(self.pg_contato)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_16.addWidget(self.label_29)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_25 = QLabel(self.pg_contato)
        self.label_25.setObjectName(u"label_25")
        sizePolicy3.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy3)

        self.horizontalLayout_13.addWidget(self.label_25)

        self.label_21 = QLabel(self.pg_contato)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_21)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_13)

        self.label_30 = QLabel(self.pg_contato)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_16.addWidget(self.label_30)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_31 = QLabel(self.pg_contato)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_17.addWidget(self.label_31)

        self.label_32 = QLabel(self.pg_contato)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_17.addWidget(self.label_32)


        self.verticalLayout_12.addLayout(self.horizontalLayout_17)

        self.Pages.addWidget(self.pg_contato)
        self.pg_editar = QWidget()
        self.pg_editar.setObjectName(u"pg_editar")
        self.horizontalLayout_21 = QHBoxLayout(self.pg_editar)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_3 = QFrame(self.pg_editar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_18 = QLabel(self.frame_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 30))
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_18)

        self.label_36 = QLabel(self.frame_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(16777215, 200))
        self.label_36.setFont(font3)
        self.label_36.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_36)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_35 = QLabel(self.frame_3)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_11.addWidget(self.label_35)

        self.txt_e_id = QLineEdit(self.frame_3)
        self.txt_e_id.setObjectName(u"txt_e_id")
        self.txt_e_id.setMaximumSize(QSize(30, 16777215))
        self.txt_e_id.setStyleSheet(u"color:rgba(211, 239, 251,1);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155,0.1);\n"
"font-family:Trebuchet MS; \n"
"font-size:21px;")

        self.horizontalLayout_11.addWidget(self.txt_e_id)

        self.label_34 = QLabel(self.frame_3)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.label_34)

        self.txt_e_nome = QLineEdit(self.frame_3)
        self.txt_e_nome.setObjectName(u"txt_e_nome")
        sizePolicy2.setHeightForWidth(self.txt_e_nome.sizePolicy().hasHeightForWidth())
        self.txt_e_nome.setSizePolicy(sizePolicy2)
        self.txt_e_nome.setStyleSheet(u"color:rgba(211, 239, 251,1);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155,0.1);\n"
"font-family:Trebuchet MS; \n"
"font-size:21px;")

        self.horizontalLayout_11.addWidget(self.txt_e_nome)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_14.addWidget(self.label_22)

        self.txt_e_comando = QLineEdit(self.frame_3)
        self.txt_e_comando.setObjectName(u"txt_e_comando")
        sizePolicy2.setHeightForWidth(self.txt_e_comando.sizePolicy().hasHeightForWidth())
        self.txt_e_comando.setSizePolicy(sizePolicy2)
        self.txt_e_comando.setStyleSheet(u"color:rgba(211, 239, 251,1);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155,0.1);\n"
"font-family:Trebuchet MS; \n"
"font-size:21px;")

        self.horizontalLayout_14.addWidget(self.txt_e_comando)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_37 = QLabel(self.frame_3)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_18.addWidget(self.label_37)

        self.txt_e_descricao = QLineEdit(self.frame_3)
        self.txt_e_descricao.setObjectName(u"txt_e_descricao")
        self.txt_e_descricao.setStyleSheet(u"color:rgba(211, 239, 251,1);\n"
"border-bottom:1px solid white;\n"
"border-radius: None;\n"
"background-color:rgba(85, 115, 155,0.1);\n"
"font-family:Trebuchet MS; \n"
"font-size:21px;")

        self.horizontalLayout_18.addWidget(self.txt_e_descricao)


        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_39 = QLabel(self.frame_3)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_19.addWidget(self.label_39)

        self.cb_e_linguagem = QComboBox(self.frame_3)
        self.cb_e_linguagem.addItem("")
        self.cb_e_linguagem.addItem("")
        self.cb_e_linguagem.addItem("")
        self.cb_e_linguagem.addItem("")
        self.cb_e_linguagem.addItem("")
        self.cb_e_linguagem.addItem("")
        self.cb_e_linguagem.addItem("")
        self.cb_e_linguagem.addItem("")
        self.cb_e_linguagem.addItem("")
        self.cb_e_linguagem.setObjectName(u"cb_e_linguagem")
        sizePolicy2.setHeightForWidth(self.cb_e_linguagem.sizePolicy().hasHeightForWidth())
        self.cb_e_linguagem.setSizePolicy(sizePolicy2)
        self.cb_e_linguagem.setFont(font4)
        self.cb_e_linguagem.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_19.addWidget(self.cb_e_linguagem)


        self.verticalLayout_4.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_22.addWidget(self.label_23)

        self.btn_salvar = QPushButton(self.frame_3)
        self.btn_salvar.setObjectName(u"btn_salvar")
        self.btn_salvar.setMinimumSize(QSize(0, 35))
        self.btn_salvar.setMaximumSize(QSize(300, 16777215))
        self.btn_salvar.setLayoutDirection(Qt.LeftToRight)
        self.btn_salvar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"    border-radius: 10px; \n"
"	font-size: 16px; \n"
"	background-color: #fff;\n"
";}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 255, 255);\n"
"	 color:black\n"
"}\n"
"\n"
"")

        self.horizontalLayout_22.addWidget(self.btn_salvar)

        self.label_26 = QLabel(self.frame_3)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_22.addWidget(self.label_26)


        self.verticalLayout_4.addLayout(self.horizontalLayout_22)


        self.horizontalLayout_21.addWidget(self.frame_3)

        self.Pages.addWidget(self.pg_editar)

        self.verticalLayout_2.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_consultar.setText(QCoreApplication.translate("MainWindow", u"CONSULTAR", None))
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">LELU</span></p><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Sistema de Anota\u00e7\u00f5es</span></p><p align=\"center\"><img src=\"imgs/logo4.png\"/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Consultar comando</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<img src=\"imgs/busca.png\"/>", None))
#if QT_CONFIG(tooltip)
        self.txt_search_cm.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.txt_search_cm.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.txt_search_cm.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.txt_search_cm.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.txt_search_cm.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.txt_search_cm.setInputMask("")
        self.txt_search_cm.setText("")
        self.txt_search_cm.setPlaceholderText(QCoreApplication.translate("MainWindow", u"busca comando", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<img src=\"imgs/busca.png\"/>", None))
        self.txt_filter_dc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"busca por descri\u00e7\u00e3o", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<img src=\"imgs/filtro.png\"/>", None))
        self.txt_filter_lg.setInputMask("")
        self.txt_filter_lg.setText("")
        self.txt_filter_lg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"filtro linguagem", None))
        self.btn_refresh.setText(QCoreApplication.translate("MainWindow", u"Atualizar tela", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Exportar para Excel", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Editar dados", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Tela de cadastro", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"imgs/cadastro.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#e6e6e6;\">CADASTRAR COMANDO</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\">Nome do Comand</span><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">o:</span></p></body></html>", None))
        self.label_5.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#dedede;\">Linha de Comando:</span></p></body></html>", None))
        self.label_10.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#e1e1e1;\">Descri\u00e7\u00e3o do comando:</span></p></body></html>", None))
        self.label_16.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#e5e5e5;\">Linguagem:</span></p></body></html>", None))
        self.cb_linguagem.setItemText(0, QCoreApplication.translate("MainWindow", u"Python", None))
        self.cb_linguagem.setItemText(1, QCoreApplication.translate("MainWindow", u"Linux", None))
        self.cb_linguagem.setItemText(2, QCoreApplication.translate("MainWindow", u"Go", None))
        self.cb_linguagem.setItemText(3, QCoreApplication.translate("MainWindow", u"Powershell", None))
        self.cb_linguagem.setItemText(4, QCoreApplication.translate("MainWindow", u"Css", None))
        self.cb_linguagem.setItemText(5, QCoreApplication.translate("MainWindow", u"Html", None))
        self.cb_linguagem.setItemText(6, QCoreApplication.translate("MainWindow", u"JavaScript", None))
        self.cb_linguagem.setItemText(7, QCoreApplication.translate("MainWindow", u"Excel", None))
        self.cb_linguagem.setItemText(8, QCoreApplication.translate("MainWindow", u"Outros", None))

        self.label_17.setText("")
        self.label_12.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_13.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"CONTATOS", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Desenvolvedor: Anderson Barrios</span></p></body></html>", None))
        self.label_27.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\"imgs/whatsApp.png\"/></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">(11)91022-7369</span></p></body></html>", None))
        self.label_28.setText("")
        self.label_29.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\"imgs/email.png\"/></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">andersonb7369@gmail.com</span></p></body></html>", None))
        self.label_30.setText("")
        self.label_31.setText("")
        self.label_32.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Tela de Edi\u00e7\u00e3o", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"imgs/botao_editar.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#e6e6e6;\">ALTERAR DADOS</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\">ID</span><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">:</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\">Nome do Comand</span><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">o:</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#dedede;\">Linha de Comando:</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#e1e1e1;\">Descri\u00e7\u00e3o do comando:</span></p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#e5e5e5;\">Linguagem:</span></p></body></html>", None))
        self.cb_e_linguagem.setItemText(0, QCoreApplication.translate("MainWindow", u"Python", None))
        self.cb_e_linguagem.setItemText(1, QCoreApplication.translate("MainWindow", u"Linux", None))
        self.cb_e_linguagem.setItemText(2, QCoreApplication.translate("MainWindow", u"Go", None))
        self.cb_e_linguagem.setItemText(3, QCoreApplication.translate("MainWindow", u"Powershell", None))
        self.cb_e_linguagem.setItemText(4, QCoreApplication.translate("MainWindow", u"Css", None))
        self.cb_e_linguagem.setItemText(5, QCoreApplication.translate("MainWindow", u"Html", None))
        self.cb_e_linguagem.setItemText(6, QCoreApplication.translate("MainWindow", u"JavaScript", None))
        self.cb_e_linguagem.setItemText(7, QCoreApplication.translate("MainWindow", u"Excel", None))
        self.cb_e_linguagem.setItemText(8, QCoreApplication.translate("MainWindow", u"Outros", None))

        self.label_23.setText("")
        self.btn_salvar.setText(QCoreApplication.translate("MainWindow", u"Salvar Altera\u00e7\u00e3o", None))
        self.label_26.setText("")
    # retranslateUi

