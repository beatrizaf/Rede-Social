class Reacao:
    def __init__(self,comentario,reacao):
        self.comentario = comentario
        self.reacao = reacao
    def menu_reacao(self,publication):
        print('1--Curti')
        print('2--Amei')
        print('3--Odiei')
        if opcao == '1':
            self.reacao = ('Curti!')
        if opcao == '2':
            self.reacao = ('Amei!')
        if opcao == '3':
             self.reacao('Odiei!')