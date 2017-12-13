import psycopg2
import psycopg2.extras

from user import User


class ContaDAO():
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_conta(self,email):
        cursor = self.conexao.cursor()
        cursor.execute('INSERT INTO tb_loguin(email, senha) VALUES (%s,%s)', (email,senha))
        cursor.close()
        self.conexao.commit()


