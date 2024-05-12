class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir(self):
        print(self.nome, self.email, self.telefone)
        

nome = str(input('Digite o seu nome: '))
email = str(input('Digite o seu email: '))
telefone = int(input('Digite o seu telefone: '))

cliente1 = Cliente(nome, email, telefone)
cliente1.exibir()