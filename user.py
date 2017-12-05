from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__user__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from genesis import Cadastrar
cadastrar=Cadastrar

class User(db.Model):
    
    nome = db.Column(db.String(100), primary_key=True)
    endereco = db.Column(db.String(1000))
    data_nsc = db.Column(db.date)
    telefone = db.Column(db.String(20))
    
    def __init__(self,nome,endereco,data_nsc,telefone,email,senha,**kwargs):
        super(User, self).__init__(**kwargs)
        self.nome = nome
        self.endereco = endereco
        self.data_nsc = data_nsc
        self.telefone = telefone
        self.amigos =[]

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    return self.menu()
    def get_endereco(self):
        return self.endereco
    def set_endereco(self, novo_endereco):
        self.endereco = novo_endereco
    return self.menu()
    def get_data_nsc(self):
        return self.data_nsc
    def set_data_nsc(self, novo_data_nsc):
        self.data_nsc = novo_data_nsc
    return self.menu()
    def get_telefone(self):
        return self.telefone
    def set_telefone(self, novo_telefone):
        self.telefone = novo_telefone
    return self.menu()
    def set_email(self, novo_email):
        genesis.email = novo_email
    return self.menu()
    def set_senha(self, nova_senha):
        genesis.senha = nova_senha
    return self.menu()

    def logar(self):
        L = input("digite o email:")
        if L in genesis.email.query.all(): 
            S = input('Digite sua senha')
            if S in genesis.Senha.query.all():                               
                return self.menu()
            else:
                print('Senha Incorreta')
                return self.logar
        else:
            print('email nao encontrado')
            return self.logar()
            
    def menu(self):
        print('1 - Editar nome')
        print('2 - Editar endereço')
        print('3 - Editar data de Nascimento')
        print('4 - editar telefone')
        print('5 - Mostrar Dados')
        print('x - Sair')
        opcao = input('Digite a opção:')

        if opcao == '1':
            novo_nome = input(str('Digite um nome:'))
            self.set_nome(novo_nome)
        if opcao == '2':
            novo_end = input(str('Digite seu endereço:(Rua, Número e Cidade)'))
            self.set_endereco(novo_end)
        if opcao == '3':
            nova_data = input('Insira sua data de nascimento:(dd/mm/aa)')
            self.set_data_nsc(nova_data)
        if opcao == '4':
            novo_tel = input(str('Digite se número de telefone:(+xx(ddd)xxxx-xxxx)'))
            self.set_telefone(novo_tel)
        if opcao == '5':
            print('Todos os Dados:' / next('Nome:', self.get_nome()) / next('Endereço:', self.get_endereco()) / next('Data de Nascimento:', self.get_data_nsc())/ next('Telefone:', self.get_telefone()))
        return opcao

db.create_all()
U = user(1, 100)
db.session.add(u)
db.session.commit()
