class Publication:
    def __init__(self,privacidade,texto,midia,localizacao):
        self.privacidade = privacidade
        self.texto = texto
        self.midia = midia
        self.localizacao = localizacao

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






