import os
from utilitarios import Cliente, ContaBancaria, clientes_informacoes

cliente1, cliente2, cliente3, cliente4, cliente5, conta_cliente1, conta_cliente2, conta_cliente3, conta_cliente4, conta_cliente5 = clientes_informacoes()

def tela_inicial():
    print('''
            ℂ𝕃𝕆𝕊𝔼𝔻 𝔹𝔸ℕ𝕂𝕀ℕ𝔾
        ''')

    print('Olá, seja bem-vindo ao CLOSED BANKING. Para entrar em sua conta, digite seu CPF e o número da conta!\n')

def login_banco():
        cpf = input('Digite o CPF do titular da conta: ').strip()
        num_conta = input('Digite o número da conta bancária: ').strip()

        
        while True:
            if cpf == '15323512394' and num_conta == '962937':
                cliente1_condicional()
                
                break
            elif cpf == '17263518393' and num_conta == '178352':

                cliente2_condicional()
                break

            elif cpf == '15392784682' and num_conta == '837182':

                cliente3_condicional()
                break

            elif cpf == '98372819474' and num_conta == '563801':

                cliente4_condicional()
                break

            elif cpf == '19898371283' and num_conta == '273102':

                cliente4_condicional()
                break
            else:
                print("CPF ou número da conta inválido.")
                cpf = input('Digite o seu CPF: ').strip()
                num_conta = input('Digite o número da sua conta bancária: ').strip()
                
def cliente1_condicional():
     
    print(f'Olá, {cliente1.nome}! Que operação deseja realizar hoje? \n')
    print('\n[1] para ver saldo')
    print('[2] para depositar')
    print('[3] para sacar')
    print('[4] para trocar de conta')
    print('[5] para sair')

    while True:
        try:
            escolha_usuario = int(input('\nDigite o número referente à operação que deseja realizar: '))
            if escolha_usuario == 1:
                print(f'O seu saldo é de R${conta_cliente1.saldo}')
            
                voltar_menu()
            elif escolha_usuario == 2:
                conta_cliente1.depositar()
                voltar_menu()
            elif escolha_usuario == 3:
                conta_cliente1.sacar()
                voltar_menu()
            elif escolha_usuario == 4:
                os.system('cls')
                login_banco()
            elif escolha_usuario == 5:
                print('Finalizando...')
                break
            else:
                print('Opção inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida! Por favor, insira um número.')

def cliente2_condicional():
     
    print(f'Olá, {cliente2.nome}! Que operação deseja realizar hoje? \n')
    print('\n[1] para ver saldo')
    print('[2] para depositar')
    print('[3] para sacar')
    print('[4] para trocar de conta')
    print('[5] para sair')

    while True:
        try:
            escolha_usuario = int(input('\nDigite o número referente à operação que deseja realizar: '))
            if escolha_usuario == 1:
                print(f'O seu saldo é de R${conta_cliente2.saldo}')
            
                voltar_menu()
            elif escolha_usuario == 2:
                conta_cliente2.depositar()
                voltar_menu()
            elif escolha_usuario == 3:
                conta_cliente2.sacar()
                voltar_menu()
            elif escolha_usuario == 4:
                os.system('cls')
                login_banco()
            elif escolha_usuario == 5:
                print('Finalizando...')
                break
            else:
                print('Opção inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida! Por favor, insira um número.')

def cliente3_condicional():
     
    print(f'Olá, {cliente3.nome}! Que operação deseja realizar hoje? \n')
    print('\n[1] para ver saldo')
    print('[2] para depositar')
    print('[3] para sacar')
    print('[4] para trocar de conta')
    print('[5] para sair')

    while True:
        try:
            escolha_usuario = int(input('\nDigite o número referente à operação que deseja realizar: '))
            if escolha_usuario == 1:
                print(f'O seu saldo é de R${conta_cliente3.saldo}')
            
                voltar_menu()
            elif escolha_usuario == 2:
                conta_cliente3.depositar()
                voltar_menu()
            elif escolha_usuario == 3:
                conta_cliente3.sacar()
                voltar_menu()
            elif escolha_usuario == 4:
                os.system('cls')
                login_banco()
            elif escolha_usuario == 5:
                print('Finalizando...')
                break
            else:
                print('Opção inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida! Por favor, insira um número.')
    
def cliente4_condicional():
     
    print(f'Olá, {cliente4.nome}! Que operação deseja realizar hoje? \n')
    print('\n[1] para ver saldo')
    print('[2] para depositar')
    print('[3] para sacar')
    print('[4] para trocar de conta')
    print('[5] para sair')

    while True:
        try:
            escolha_usuario = int(input('\nDigite o número referente à operação que deseja realizar: '))
            if escolha_usuario == 1:
                print(f'O seu saldo é de R${conta_cliente4.saldo}')
            
                voltar_menu()
            elif escolha_usuario == 2:
                conta_cliente4.depositar()
                voltar_menu()
            elif escolha_usuario == 3:
                conta_cliente4.sacar()
                voltar_menu()
            elif escolha_usuario == 4:
                os.system('cls')
                login_banco()
            elif escolha_usuario == 5:
                print('Finalizando...')
                break
            else:
                print('Opção inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida! Por favor, insira um número.')

def cliente5_condicional():
     
    print(f'Olá, {cliente5.nome}! Que operação deseja realizar hoje? \n')
    print('\n[1] para ver saldo')
    print('[2] para depositar')
    print('[3] para sacar')
    print('[4] para trocar de conta')
    print('[5] para sair')

    while True:
        try:
            escolha_usuario = int(input('\nDigite o número referente à operação que deseja realizar: '))
            if escolha_usuario == 1:
                print(f'O seu saldo é de R${conta_cliente5.saldo}')
            
                voltar_menu()
            elif escolha_usuario == 2:
                conta_cliente5.depositar()
                voltar_menu()
            elif escolha_usuario == 3:
                conta_cliente5.sacar()
                voltar_menu()
            elif escolha_usuario == 4:
                os.system('cls')
                login_banco()
            elif escolha_usuario == 5:
                print('Finalizando...')
                break
            else:
                print('Opção inválida. Tente novamente.')
        except ValueError:
            print('Entrada inválida! Por favor, insira um número.')

def voltar_menu():
        input('\nDigite qualquer tecla para voltar ao menu principal!\n ')
        cliente1_condicional()

    
def main():
    os.system('cls')
    tela_inicial()
    login_banco()

if __name__ == '__main__':
    main()