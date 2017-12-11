class Perfil:
    def __init__(self,foto,bibliografia):
        self.foto = foto
        self.biblio = bibliografia

    def get_foto(self):
        return self.foto
    def set_foto(self, nova_foto):
        self.foto = nova_foto

    def get_biblio(self):
        return self.biblio
    def set_biblio(self, nova_biblio):
        self.biblio = nova_biblio
#colocar em usuario
#tipo foto é o blob
