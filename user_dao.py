import psycopg2
import psycopg2.extras

from user import User


class ContaDAO():
    def __init__(self, conexao):
        self.conexao = conexao

    def inserir_email(self):
        cursor = self.conexao.cursor()
        cursor.execute('INSERT INTO tb_email(email) VALUES (%s)', (user.email))
        cursor.close()
        self.conexao.commit()
	
	def inserir_senha(self):
        cursor = self.conexao.cursor()
        cursor.execute('INSERT INTO tb_senha(email) VALUES (%s)', (user.senha))
        cursor.close()
        self.conexao.commit()
	