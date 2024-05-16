from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    cpf: str
    endereço: str
    telefone:str
    email: str

class ContaBancaria:
    cliente: Cliente
    numero_conta: int
    saldo: 0

    def exibir_nome_cliente(self):
        return self.cliente.nome
    
    def exibir_saldo_cliente(self):
        return self.saldo
    
    def exibir_email_cliente(self):
        return self.cliente.email
    
    def exibir_cpf_cliente(self):
        return self.cliente.cpf
    
    def sacar(self):
        valor = int(input('Digite o valor que queira sacar: R$'))
        self.saldo -= valor