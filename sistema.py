from acounts import Bd
from acounts import Conta
from acounts import Loguin
banco = Bd()
class Sistem:
    def __init__(self):
        pass
    def loguin(self,e,s):
        for x in banco.loguin:
            pass
            #como acessar ***

    def menu(self):
        print('1 - Cadastrar conta')
        print('2 - Loguin')
        print('x - Sair')
        opcao = input('Digite a opção: ')

        if opcao == '1':
            usuario = Conta
            log = Loguin
            usuario.nome = input('Digite seu nome: ')
            usuario.idade = input('Digite sua idade: ')
            usuario.telefone = input('Digite seu telefone: ')
            usuario.endereco = input('Digite seu endereço: ')
            log.email = input('Digite seu email: ')
            log.senha = input('Digite sua senha: ')
            banco.insert_user(usuario,log)
            #como acessar os dados para efetuar loguin
        if opcao == 2:
                pass


        return(opcao)
