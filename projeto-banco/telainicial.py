import os
from utilitarios import Cliente, ContaBancaria, clientes_informacoes

def tela_inicial():
    print('''
            ℂ𝕃𝕆𝕊𝔼𝔻 𝔹𝔸ℕ𝕂𝕀ℕ𝔾
        ''')

    print('Olá, seja bem-vindo ao CLOSED BANKING. Para entrar em sua conta, digite seu CPF e o número da conta!\n')

def login_banco():
        cpf = input('Digite o CPF do titular da conta: ').strip()
        num_conta = input('Digite o número da conta bancária: ').strip()

        cliente1, cliente2, conta_cliente1, conta_cliente2 = clientes_informacoes()
        while True:
            if cpf == '15323512394' and num_conta == '962937':
                print(f'Olá, {cliente1.nome}. Seja bem-vindo!')
                conta_cliente1.saldo_inicial()
                break
            elif cpf == '17263518393' and num_conta == '178352':
                print(f'Olá, {cliente2.nome}. Seja bem-vinda!')
                conta_cliente2.saldo_inicial()
                break
            else:
                print("CPF ou número da conta inválido.")
                cpf = input('Digite o seu CPF: ').strip()
                num_conta = input('Digite o número da sua conta bancária: ').strip()

def main():
    os.system('cls')
    tela_inicial()
    login_banco()

if __name__ == '__main__':
    main()