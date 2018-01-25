from batepapo import Batepapo
bp = Batepapo
class Perfil:
    def __init__(self):
        self.bibliografia = str
        self.amigos = list
        self.notificacao = list

    def menu_feed(self):
        print('\n\n')
        print('Bem vindo')
        print('1 - Editar Bibliografia')
        print('2 - Abrir bate papo')
        print('3 - Ver perfil')
        print('x - Sair')
        opcao = input('Digite a opção: ')

        if opcao == '1':
            print('Digite algo sobre você para que os outros possam lhe conhecer melhor!')
            self.bibliografia = input('Digite: ')
        if opcao == '2':
            opcao = ''
            while opcao != 'x':
                opcao = bp.menu(None)
        if opcao == '3':
            print(self.bibliografia)
            c = 0
            for x in self.amigos:
                c+=1
            print('amigos =',c)

        return(opcao)
