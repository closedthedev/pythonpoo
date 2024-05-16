from dataclasses import dataclass
import os

@dataclass
class CaixaEletronico():

    cliente: str
    saldo: int
    

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

    def ver_saldo(self):
        print(f'O seu saldo atual é de: R${self.saldo}')

def voltar_menu():
        input('Digite qualquer tecla para voltar ao menu principal!\n ')
        main()

caixa = CaixaEletronico('Luiz Otavio' , 1300)
def exibir_opções():
    print(f'Olá, {caixa.cliente}. Que operação deseja realizar hoje? ')
    print('\n[1] para ver saldo')
    print('[2] para depositar')
    print('[3] para sacar')
    print('[0] para sair')
    
def exibir_escolhas():
    while True:
        try:
            escolha_usuario = int(input('\nDigite o número referente à operação que deseja realizar: '))
            if escolha_usuario == 1:
                caixa.ver_saldo()
                voltar_menu()
            elif escolha_usuario == 2:
                caixa.depositar()
                voltar_menu()
            elif escolha_usuario == 3:
                caixa.sacar()
                voltar_menu()
            elif escolha_usuario == 0:
                print('Finalizando...')
                break
            else:
                print('Opção inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida! Por favor, insira um número.')


def main():
    os.system('cls')
    exibir_opções()
    exibir_escolhas()

if __name__ == '__main__':
    main()
    