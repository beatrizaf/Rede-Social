class User:
    def __init__(self,nome,endereco,data_nsc,telefone,email,senha):
        self.nome = nome
        self.endereco = endereco
        self.data_nsc = data_nsc
        self.telefone = telefone
        self.email = email
        self.senha = senha

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, novo_endereco):
        self.endereco = novo_endereco

    def get_data_nsc(self):
        return self.data_nsc

    def set_data_nsc(self, novo_data_nsc):
        self.data_nsc = novo_data_nsc

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def set_email(self, novo_email):
        self.email = novo_email

    def set_senha(self, nova_senha):
        self.senha = nova_senha

    def menu(self):
        print('1 - Editar nome')
        print('2 - Editar endereço')
        print('3 - Editar data de Nascimento')
        print('4 - editar telefone')
        print('5 - Mostrar Dados')
        print('x - Sair')
        opcao = input('Digite a opção:')

        if opcao == '1':
            novo_nome = input(str('Digite um nome:'))  # coigir o uso da fucão set baseado em outro codigos
            set_nome(novo_nome)
        if opcao == '2':
            novo_end = input(str('Digite seu endereço:(Rua, Número e Cidade)'))

        if opcao == '3':
            nova_data = input(str('Insira sua data de nascimento:(dd/mm/aa)'))

        if opcao == '4':
            novo_tel = input(str('Digite se número de telefone:(+xx(ddd)xxxx-xxxx)'))

        if opcao == '5':
            print('Todos os Dados:' / next('Nome:', get_nome()) / next('Endereço:', )  # verificar utilização do get

    return opcao

    def logar(self):
        resposta = str
        while (resposta != 'loguin efetuado'):
            e = input("Insira o email:")
            s = input("Senha:")
            if e == self.email and s == self.senha:
                print('Loguin efetuado')
                # chamar menu de opções
                # criar

            else:
                print('email ou senha incorretos')
                respoata = ('email ou senha incorretos')
