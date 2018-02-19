from batepapo import *
from acounts import *
log = Bd()
bp = Batepapo()
class Perfil:
    def __init__(self):
        self.bibliografia = str
        self.amigos = list
        self.notificacao = list

    def menu_feed(self,emai,senh,n,i,t,e):
        print('\n\n')
        print('Bem vindo')
        print('1 - Editar Bibliografia')
        print('2 - Abrir bate papo')
        print('3 - Ver perfil')
        print('4 - Mudar email e senha')
        print('x - Sair')
        opc = input('Digite a opção: ')

        if opc == '1':
            print('Digite algo sobre você para que os outros possam lhe conhecer melhor!')
            self.bibliografia = input('Digite: ')
        if opc == '2':
            pass
            opca = ''
            while opca != 'x':
               opca = bp.menu()
        if opc == '3':
            perf = log.contas
            print(self.bibliografia)
            c = 0
            for x in self.amigos():
                c+=1
                print(perf.nome,perf.idade,perf.telefone,perf.endereco)
            print('amigos =',c)
        if opc == '4':
            for x in log.loguin.email:
                if x == emai:
                    log.loguin.email[x] = input('digite seu novo email: ')
            for y in log.loguin.senha:
                if y == senh:
                   log.loguin.senha[y] = input('digite sua nova senha: ')
        return(opc)
