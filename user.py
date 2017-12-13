class User: 
    def __init__(self):
        self.nome = ''
        self.endereco = ''
        self.data_nsc = ''
        self.telefone = ''
        self.amigos = []
        self.lista_email = []
        self.lista_senha = []

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
        genesis.email = novo_email

    def set_senha(self, nova_senha):
        genesis.senha = nova_senha

    def inicio(self):
        print('1-Fazer Loguin')
        print('2-Fazer Cadastro')
        opcao1 = input('Digite a Opção:')
        if opcao1 == '1' :
            if L in lista_email:
                S = input('Digite sua senha')
                if S in senha_email:
                    self.menu()
                else:
                    print('Senha Incorreta')
                    self.logar()
            else:
                print('email nao encontrado')
                self.logar()
        elif opcao1 == '2':
            print('Criar conta:')
            Loguin = input('Digite um email:')
            Senha = input('Digite uma senha')
            self.lista_email.append(Loguin)
            self.lista_senha.append(Senha)
            self.inicio()



    def menu(self):
        print('1 - Editar nome')
        print('2 - Editar endereço')
        print('3 - Editar Data de Nascimento')
        print('4 - editar Telefone')
        print('5 - Mostrar Dados')
        print('6 - Acessar Perfil')
        print('x - Sair')
        opcao = input('Digite a opção:')

        if opcao == '1':
            novo_nome = input(str('Digite um nome:'))
            self.set_nome(novo_nome)
        if opcao == '2':
            novo_end = input(str('Digite seu endereço:(Rua, Número e Cidade)'))
            self.set_endereco(novo_end)
        if opcao == '3':
            nova_data = input('Insira sua data de nascimento:(dd/mm/aa)')
            self.set_data_nsc(nova_data)
        if opcao == '4':
            novo_tel = input(str('Digite se número de telefone:(+xx(ddd)xxxx-xxxx)'))
            self.set_telefone(novo_tel)
        if opcao == '5':
            print('Todos os Dados:' / next('Nome:', self.get_nome()) / next('Endereço:', self.get_endereco()) / next('Data de Nascimento:', self.get_data_nsc())/ next('Telefone:', self.get_telefone()))
        return opcao
