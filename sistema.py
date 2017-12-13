from user_dao import user_dao
import psycopg2

class sistema:
    def __init__(self):
        conexao = psycopg2.connect(host="localhost", database="****", user="postgres", password="1111")
        self.User_dao = ContaDAO(conexao)
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
            self.email = Loguin
            self.senha = Senha
            self.inicio()
            self.UserDAO.inserir_conta(email,senha)
