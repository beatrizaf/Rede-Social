import psycopg2
class User:

    def __init__(self):
        conexao = psycopg2.connect(host="localhost", database="##", user="postgres", password="postgres")
        self.UserDAO = UserDAO(conexao)
        self.nome = ''
        self.endereco = ''
        self.data_nsc = ''
        self.telefone = ''
        self.amigos = None
        self.email = None
        self.senha = None


    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_endereco(self):
        return self.endereco
    def set_endereco(self, novo_endereco):
        self.endereco = novo_endereco

    def get_data_nsc(self):
        return self.data_nsc
    def set_data_nsc(self, novo_data_nsc):
        self.data_nsc = novo_data_nsc

    def get_telefone(self):
        return self.telefone
    def set_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def menu(self):
        print('1 - Editar nome')
        print('2 - Editar endereço')
        print('3 - Editar Data de Nascimento')
        print('4 - editar Telefone')
        print('5 - Mostrar Dados')
        print('6 - Acessar Perfil')
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
        if opcao == '6':

        return opcao
