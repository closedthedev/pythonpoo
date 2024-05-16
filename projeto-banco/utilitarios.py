from dataclasses import dataclass
import random

@dataclass
class Cliente:
    nome: str
    cpf: str
    email: str
@dataclass
class ContaBancaria:
    cliente: Cliente
    numero_conta: str
    saldo: float = 0.0

    def exibir_nome_cliente(self):
        return self.nome
    
    
    def exibir_email_cliente(self):
        return self.email
    
    def exibir_cpf_cliente(self):
        return self.cpf
    

    def depositar(self):
        while True:
            try:
                valor = int(input('Quanto você quer depositar? R$'))
                if valor > 0:
                    self.saldo += valor
                    print(f'Depósito concluído com sucesso. Novo saldo: R${self.saldo}')
                    break  
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


def clientes_informacoes():
    saldo_inicial = random.randint(500,5000) 
    cliente1 = Cliente(nome='Luiz Otavio', cpf='15323512394', email='closedthedev@gmail.com')
    cliente2 = Cliente(nome='Rafaela', cpf='17263518393', email='rafaelathedev@gmail.com')

    conta_cliente1 = ContaBancaria(cliente=cliente1, numero_conta='962937', saldo=saldo_inicial )
    conta_cliente2 = ContaBancaria(cliente=cliente2, numero_conta='178352', saldo=saldo_inicial)

    # Retorna as instâncias dos clientes
    return cliente1, cliente2, conta_cliente1, conta_cliente2

# Chamando a função para criar as instâncias
cliente1, cliente2, conta_cliente1, conta_cliente2 = clientes_informacoes()

