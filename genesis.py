class Cadastrar:
    def __init__(self):
        self.lista_email = []
        self.lista_senha = []

    def criar_conta(self):
        print('Criar conta:')
        Loguin = input('Digite um email:')
        Senha = input('Digite uma senha')
        self.lista_email.append(Loguin)
        self.lista_senha.append(Senha)
