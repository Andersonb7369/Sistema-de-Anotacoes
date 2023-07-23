import sqlite3

class DataBase():
    def __init__(self, name="banco.db") -> None:
        self.name = name

    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS users(

                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    user TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    access TEXT NOT NULL
                );
            """)
        except AttributeError:
            print("faça a conexão")

    def insert_user(self, name, user, password, access):

        cursor = self.connection.cursor()
        cursor.execute("""

            INSERT INTO users(name, user, password, access) VALUES(?,?,?,?)

        """, (name, user, password, access))
        self.connection.commit()

    def check_user(self, password):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM users;
            """)

            for linha in cursor.fetchall():
                if linha[3] == password:
                    return "administrador"
                else:
                    continue
            return "sem acesso"
        except:
            pass


    def create_table(self):

        cursor = self.connection.cursor()

        cursor.execute(f"""

            CREATE TABLE IF NOT EXISTS notes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            n_comando TEXT NOT NULL,
            l_comando TEXT NOT NULL,
            descricao TEXT NOT NULL,
            linguagem TEXT NOT NULL
            );
        """)

    def insert(self, nome, comando, descricao, linguagem):

        cursor = self.connection.cursor()
        campos_tabela = ('n_comando', 'l_comando', 'descricao', 'linguagem')
        cursor.execute(f"""INSERT INTO notes {campos_tabela} VALUES (?,?,?,?)""",(nome, comando, descricao, linguagem))

        self.connection.commit()

    def update(self, ide, l_comando, descricao):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""UPDATE notes SET l_comando = '{l_comando}', 
            descricao ='{descricao}' WHERE id =  '{ide}'""")
            self.connection.commit()

        except AttributeError:
            print("faça a conexão para alterar campos")

    def update_del(self, ide):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""DELETE FROM notes WHERE id = {ide}""")
            self.connection.commit()

        except AttributeError:
            print('faça a conexão para alterar campos.')


if __name__ == "__main__":
    db = DataBase()
    db.conecta()
    db.create_table_users()
    db.create_table()
    db.close_connection()

#import io
#conn = sqlite3.connect('banco.db')
#with io.open('banco_dump.sql', 'w') as f:
#    for linha in conn.iterdump():
#        f.write('%s\n' % linha)

