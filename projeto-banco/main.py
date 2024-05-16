from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    cpf: str
    email: str

class ContaBancaria:
    cliente: Cliente
    numero_conta: int
    saldo: int = 0

    def exibir_nome_cliente(self):
        return self.cliente.nome
    
    
    def exibir_email_cliente(self):
        return self.cliente.email
    
    def exibir_cpf_cliente(self):
        return self.cliente.cpf
    
    def saldo_inicial(self):
        while True:
            try:
                saldo_inicial = int(input('Digite seu saldo inicial: R$'))
                if saldo_inicial > 0:
                    self.saldo = saldo_inicial
                    break
            except ValueError:
                 print("Erro: Por favor, insira um valor numérico válido.\n")

    def depositar(self):
        while True:
            try:
                valor = int(input('Quanto você quer depositar? R$'))
                if valor > 0:
                    self.saldo += valor
                    print(f'Depósito concluído com sucesso. Novo saldo: R${self.saldo}')
                    break  # Saia do loop somente se o depósito for bem-sucedido
                else:
                    print('Valor de depósito inválido! Por favor, insira um valor positivo.')
            except ValueError:
                 print("Erro: Por favor, insira um valor numérico válido.\n")

    
    def sacar(self):
        while True:
            try:
                valor = int(input('Quanto você quer sacar? R$'))
                if valor > 0 and valor <= self.saldo:
                    self.saldo -= valor
                    print(f'Saque realizado com sucesso. Novo saldo: R${self.saldo}')
                    break
                elif valor > self.saldo:
                    print('Saldo insuficiente. Por favor, insira um valor menor.')
                else:
                    print('Valor incorreto! Por favor, insira um valor positivo.')
            except ValueError:
                print("Erro: Por favor, insira um valor numérico válido.")



cliente1 = Cliente(nome = 'Luiz Otavio' , cpf = '15323512394', email = 'closedthedev@gmail.com')
cliente2 = Cliente(nome = 'Rafaela' , cpf = '17263518393', email = 'rafaelathedev@gmail.com')

conta1 = ContaBancaria(cliente=cliente1, numero_conta=962937)
conta2 = ContaBancaria(cliente=cliente2, numero_conta=178352)
