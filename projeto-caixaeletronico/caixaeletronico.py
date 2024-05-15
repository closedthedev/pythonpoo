from dataclasses import dataclass
import os

@dataclass
class CaixaEletronico():

    cliente: str
    saldo: int
    

    def depositar(self):

        valor = int(input('Quanto você quer depositar? '))

        if valor > 0:
            self.saldo += valor
            print(f'Depósito concluído com sucesso. ')

        else:
            print('Valor de depósito inválido!')

    def sacar(self):

        valor = int(input('Quanto você quer sacar? '))

        if valor > 0 and valor <= self.saldo:

            self.saldo -= valor
            print('Saque realizado com sucesso.')

        elif valor > self.saldo:
            print('Saldo insuficiente.') 

        else: print('Valor incorreto!')

    def ver_saldo(self):
        print(f'O seu saldo disponível é de: {self.saldo}')

def voltar_menu():
        input('Digite qualquer tecla para voltar ao menu principal!\n ')
        main()

caixa = CaixaEletronico('Luiz Otavio' , 1300)
def exibir_opções():
    print(f'Olá, {caixa.cliente}. Que operação deseja realizar hoje? ')
    print('\n[1] para ver saldo')
    print('[2] para depositar')
    print('[3] para sacar')
def exibir_escolhas():
    escolha_usuário = int(input('\nDigite o número referente a operação que deseja realizar: '))

    if escolha_usuário == 1:
        caixa.ver_saldo()
        voltar_menu()

    elif escolha_usuário ==2:
        caixa.depositar()
        caixa.ver_saldo()
        voltar_menu()

    elif escolha_usuário ==3:
        caixa.sacar()
        caixa.ver_saldo()
        voltar_menu()




def main():
    os.system('cls')
    exibir_opções()
    exibir_escolhas()

if __name__ == '__main__':
    main()
    