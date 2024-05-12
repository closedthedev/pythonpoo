#criando uma classe, mas agora utilizando o dataclass para facilitar

from dataclasses import dataclass


@dataclass
class Cliente:
    nome: str
    email: str
    telefone: int

cliente1 = Cliente(nome='Luiz' , email = 'closedferreir@gmail.com', telefone ='21966454645' , )

print(cliente1.nome , cliente1.email , cliente1.telefone)