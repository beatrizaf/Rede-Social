class Publication:
    def __init__(self,privacidade,texto,midia,localizacao,link):
        self.privacidade = privacidade
        self.texto = texto
        self.midia = midia
        self.localizacao = localizacao
        self.link = link
        self.comentario = comentario
        self.reacao = reacao

    def get_privacidade(self):
        return self.privacidade
    def set_privacidade(self, nova_termo_priv):
        self.privacidade = nova_termo_priv

    def get_texto(self):
        return self.texto
    def set_texto(self,novo_txt):
        self.texto = novo_txt

    def get_midia(self):
        return self.midia
    def set_midia(self, nova_midia):
        self.midia = nova_midia

    def get_localizacao(self):
        return self.localizacao
    def set_localizacao(self, nova_localizacao):
        self.localizacao = nova_localizacao

    def get_comentario(self):
        return self.comentario
    def set_comentario(self, novo_comentario):
        self.comentario = novo_comentario 

    def menu_reacao(self):
        print('1--Curti')
        print('2--Amei')
        print('3--Odiei')
        if opcao == '1':
            self.reacao = ('Curti!')
        if opcao == '2':
            self.reacao = ('Amei!')
        if opcao == '3':
            self.reacao = ('Odiei!')
