from sistema import Sistem
sis = Sistem()
class Batepapo:
    def __init__(self):
        self.conversas = list
    def menu(self):
        print('\n\n')
        print('Bate papo')
        print('1 - Nova conversa')
        print('2 - Ver todas as conversas')
        print('3 - Nova menssagem')
        print('x - Sair')
        opcao = input('Digite a opção: ')

        if opcao == '1':
           mensagem.nova_conversa(None)
        if opcao == '2':
            for x in self.conversas():
                print(x)
        if opcao == '3':
            mensagem.nova_msg(None)
        return (opcao)
class Conversa:
    def __init__(self):
        self.menssagens = list

class mensagem:
    def __init__(self):
        self.texto = str

    def nova_conversa(self):
        destino = input('Digite o nome do destinatario: ')
        for x in sis.contas:
            if x.nome == destino:
                txt = self.texto
                new_con = Conversa()
                new_con.menssagens.append(txt)
    def nova_msg(self):
        destino = input('Digite o nome do outro prosador: ')
        new_ms = mensagem()
        con = Batepapo()
        for x in con.conversas:
            if x.nome == destino:
                for y in x:
                    print(y)
                new_ms.texto = input('Digite a menssagem: ')
                x.append(new_ms.texto)
