class Conta:
    def __init__(self):
        self.nome = str
        self.idade = int
        self.telefone = str
        self.endereco = str

class Loguin:
    def __init__(self):
        self.email = str
        self.senha =str

class Bd:
    def __init__(self):
        self.contas = []
        self.loguin = []

    def insert_user(self,user,log):
        self.contas.append(user)
        self.loguin.append(log())
