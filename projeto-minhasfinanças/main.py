from utilitarios import (
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total,
)

#cadastrando categorias

categoria_receita = cadastrar_categoria('Receitas')
categoria_conta = cadastrar_categoria('Contas fixas')
categoria_lazer = cadastrar_categoria('Lazer')
categoria_viagem = cadastrar_categoria('Viagem')


#cadastrando as transações

cadastrar_transacao(descrição = 'Salário Jun/2024' , valor = 1700 , categoria =  categoria_receita) 
cadastrar_transacao(descrição = 'Venda Celular' , valor = 1200 , categoria =  categoria_receita)
cadastrar_transacao(descrição = 'Conta de luz' , valor = -550 , categoria =  categoria_conta)
cadastrar_transacao(descrição = 'Viagem Arraial do Cabo' , valor = -300 , categoria =  categoria_viagem)
cadastrar_transacao(descrição = 'Cinema' , valor = -150 , categoria =  categoria_lazer)

total = saldo_total()

print(f'Seu saldo final é de {total}')
    
    