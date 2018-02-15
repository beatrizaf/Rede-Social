from batepapo import Batepapo
bp = Batepapo()
class Perfil:
    def __init__(self):
        self.bibliografia = str
        self.amigos = list
        self.notificacao = list

    def menu_feed(self,email,senha):
        print('\n\n')
        print('Bem vindo')
        print('1 - Editar Bibliografia')
        print('2 - Abrir bate papo')
        print('3 - Ver perfil')
        print('x - Sair')
        opc = input('Digite a opção: ')

        if opc == '1':
            print('Digite algo sobre você para que os outros possam lhe conhecer melhor!')
            self.bibliografia = input('Digite: ')
        if opc == '2':
            pass
            opca = ''
            while opca != 'x':
               opca = bp.menu(None)
        if opc == '3':
            print(self.bibliografia)
            c = 0
            for x in self.amigos():
                c+=1
            print('amigos =',c)

        return(opc)
