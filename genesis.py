from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__email_senha__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Cadastrar(db.Model):
        
    email = db.Column(db.String(100), primary_key=True)
    senha = db.Column(db.String(18))

    def __init__(self,**kwargs):
        super(Cadastra, self).__init__(**kwargs)
        self.lista_email = []
        self.lista_senha = []

    def criar_conta(self):
        print('Criar conta:')
        Loguin = input('Digite um email:')
        Senha = input('Digite uma senha')
        self.lista_email.append(Loguin)
        self.lista_senha.append(Senha)

db.create_all()
db.session.add()
