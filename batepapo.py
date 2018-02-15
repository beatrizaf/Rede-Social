from acounts import Bd
con = Bd()
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
        opca = input('Digite a opção: ')

        if opca == '1':
           mensagem.nova_conversa(None)
        if opca == '2':
            for x in self.conversas():
                print(x)
        if opca == '3':
            mensagem.nova_msg(None)
        return (opca)
class Conversa:
    def __init__(self):
        self.menssagens = list

class mensagem:
    def __init__(self):
        self.texto = str

    def nova_conversa(self):
        destino = input('Digite o nome do destinatario: ')
        for x in con.contas:
            if x.nome == destino:
                txt = self.texto
                new_con = Conversa()
                new_con.menssagens.append(txt)
    def nova_msg(self):#passar a lista de conversas como argumento
        destino = input('Digite o nome do outro prosador: ')
        new_ms = mensagem()
        for x in self.conversas:
            if x.nome == destino:
                for y in x:
                    print(y)
                new_ms.texto = input('Digite a menssagem: ')
                x.append(new_ms.texto)
