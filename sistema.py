from acounts import Conta
from acounts import Loguin
from sistema_feed import Perfil
perf = Perfil
class Sistem:
    def __init__(self):
        self.contas = []
        self.loguin = []
    def cadastrar_user(self,nome,idade,telefone,endereco,email,senha):      #Pedir ajuda no IF
        conta = Conta(nome,idade,telefone,endereco)
        log = Loguin(email,senha)
        self.contas.append(conta)
        self.loguin.append(log)
    def menu(self):
        print('1 - Cadastrar conta')
        print('2 - Loguin')
        print('x - Sair')
        opcao = input('Digite a opção: ')

        if opcao == '1':
            nome = input('Digite seu nome: ')
            idade = input('Digite sua idade: ')
            telefone = input('Digite seu telefone: ')
            endereco = input('Digite seu endereço: ')
            email = input('Digite seu e-mail:')
            for email1 in self.loguin:
                if email1 == email:
                    print('E-mail já cadastrado')
                    return(opcao)
            senha = input('Digite sua senha:')
            senha1 = input('Digite sua senha novamente:')
            if senha != senha1:
                print('As senhas não conferem')
                senha = input('Digite sua senha: ')
                senha1 = input('Digite sua senha novamente: ')
            self.cadastrar_user(nome,idade,telefone,endereco)


        if opcao == 2:
                email = input('Digite seu e-mail: ')
                senha = input('Digite sua senha: ')
                for usuario in self.loguin:
                    if usuario.email == email and usuario.senha == senha:
                        print('Loguin efetuado!')
                        opcao = ''
                        while opcao != 'x':
                            opcao = perf.menu_feed(None)
                    else:
                        print('Email ou senha incorreto!')

        return(opcao)






