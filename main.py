import os
import re
import sqlite3
import sys
import pandas as pd
from PySide2.QtGui import QIcon
from PySide2.QtSql import QSqlDatabase, QSqlTableModel
from PySide2.QtWidgets import (QApplication, QMainWindow, QMessageBox, QWidget)
from PySide2.QtCore import Qt, QAbstractTableModel, QModelIndex, QItemSelectionModel
from database import DataBase
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
#from cad_user import Cad_Login
#from ui_cad_login import Ui_cad_Login


#######################----------FIM DA IMPORTAÇÕES------------#########################################

class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")
        appIcon = QIcon('imgs/logo4.png')
        self.setWindowIcon(appIcon)
        # função atribuida ao botao
        self.btn_login.clicked.connect(self.checkLogin)

    def checkLogin(self):
        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.check_user(self.txt_password.text())

        if autenticado.lower() == "administrador":
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Senha incorreta \n \n Tentativa: {self.tentativas + 1} de 3')
                msg.exec_()
                self.tentativas += 1
            if self.tentativas == 3:
                # bloquear o usuário
                self.users.close_connection()
                sys.exit(0)

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self.data = data

    def rowCount(self, parent=QModelIndex()):
        return len(self.data)

    def columnCount(self, parent=QModelIndex()):
        return len(self.data[0])

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self.data[index.row()][index.column()])
        return None

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento")
        appIcon = QIcon('imgs/logo4.png')
        self.setWindowIcon(appIcon)

        def abrir_banco():
            # Abrindo o banco de dados
            db = QSqlDatabase("QSQLITE")
            db.setDatabaseName("banco.db")
            db.open()

            # Criar o modelo de dados da tabela
            self.model = QSqlTableModel(db=db)
            self.model.setTable("notes")
            self.tb_geral.setModel(self.model)
            self.model.select()

            # *************PAGINAS DO SISTEMA***********************************************
            self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
            self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
            self.btn_consultar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_consultar))
            self.btn_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))

            # filtro
            self.txt_search_cm.textChanged.connect(self.update_search)
            self.txt_filter_lg.textChanged.connect(self.update_filter)
            self.txt_filter_dc.textChanged.connect(self.update_descr)
            self.btn_excel.clicked.connect(self.csv_file)
            self.btn_cadastrar.clicked.connect(self.inserir)
            self.btn_refresh.clicked.connect(abrir_banco)

            # botao cadastar comando
            self.btn_salvar.clicked.connect(self.salvar_dados)
            self.btn_salvar.clicked.connect(abrir_banco)
            self.btn_salvar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_consultar))

            # Carregar dados
            self.btn_edit.clicked.connect(self.selecionar_dados)
            self.btn_edit.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_editar))
            self.btn_salvar.clicked.connect(self.salvar_dados)
            # self.btn_load.clicked.connect(self.carregar_linha)

            # Criar o seletor de itens da tabela e conectar o sinal de seleção
            self.selection_model = self.tb_geral.selectionModel()
            self.selection_model.selectionChanged.connect(self.selecionar_dados)

            self.reset_table()

        abrir_banco()

    def inserir(self):

        nome = self.txt_nome.text()
        comando = self.txt_comando.text()
        descricao = self.txt_descricao.text()
        linguagem = self.cb_linguagem.currentText()
        db = DataBase()
        db.conecta()
        db.insert(nome, comando, descricao, linguagem)
        db.close_connection()

        # mensagem de confirmação
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de comando")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()
        # resetando os campos para novo cadastro
        self.txt_nome.setText("")
        self.txt_comando.setText("")
        self.txt_descricao.setText("")
        self.reset_table()

    def table_geral(self):

        self.tb_geral.setStyleSheet(u" QHeaderView{ color:black}; color:#fff;font-size: 15px;")
        for i in range(1, 5):
            self.tb_geral.resizeColumnToContents(i)

    def ler_bd(self, linha_id):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes WHERE id = ?", (linha_id + 1,)) # corrige o ID da tabela

    # Armazena a linha selecionada em uma variável
        linha = cursor.fetchone()  # Isso retorna a linha do resultado da consulta
        return linha

    def selecionar_dados(self):
        try:
    # Verificar se há uma linha selecionada na tabela
            indexes = self.selection_model.selectedIndexes()
            row = indexes[0].row()  # Obter o número da linha selecionada
            data_row = self.ler_bd(row) # Salva a linha selecionada na variavel
            data_row1 = list(data_row) # tranforma a tupla em lista
            print(data_row1)
    # envia os dados da linha para editar
            self.txt_e_id.setText(str(data_row1[0]))
            self.txt_e_nome.setText(data_row1[1])
            self.txt_e_comando.setText(data_row1[2])
            self.txt_e_descricao.setText(data_row1[3])
        except:
            pass

    def salvar_dados(self):
        try:
        # armazena os campos nas variaveis
            id_comando = self.txt_e_id.text()
            n_comando = self.txt_e_nome.text()
            l_comando = self.txt_e_comando.text()
            descricao = self.txt_e_descricao.text()

        # Conecta e grava as aletrações no id indicado
            conn = sqlite3.connect('banco.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE notes SET n_comando = ?, l_comando = ?, descricao = ? WHERE id = ?", (n_comando, l_comando, descricao, id_comando))
            conn.commit()
            conn.close()

        # Limpa os campos após a alterar
            self.txt_e_id.clear()
            self.txt_e_nome.clear()
            self.txt_e_comando.clear()
            self.txt_e_descricao.clear()

        # Confirma com uma mensagem
            #msg = QMessageBox()
            #msg.setIcon(QMessageBox.Information)
            #msg.setWindowTitle("Alteração")
            #msg.setText("Alteração realizada com sucesso!")
            #msg.exec_()
        except:
            print('deu erro')

    def reset_table(self):
        self.table_geral()

    def update_search(self, s):
        s = re.sub("[\W_]+", "", s)
        filter_str = 'n_comando LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)

    def update_filter(self, s):
        s = re.sub("[\W_]+", "", s)
        filter_str = 'linguagem LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)

    def update_descr(self, s):
        s = re.sub("[\W_]+", "", s)
        filter_str = 'descricao LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)

    def csv_file(self):
        user = os.path.join(os.environ['USERPROFILE'], 'Documents')
        cnx = sqlite3.connect('banco.db')
        result = pd.read_sql_query("SELECT * FROM notes", cnx)
        #result.to_csv(f"{user}\Export.csv")
        result.to_excel(f"{user}\export.xlsx", sheet_name='notes', index=False)


        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Relatório")
        msg.setText(f"Exportado para: {user}\Export.csv")
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    #window = MainWindow()
    window.show()
    app.exec_()
