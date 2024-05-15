from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int
    sexo: str


pessoa1 = Pessoa('Rafaela' , 22 , 'feminino')
pessoa2 = Pessoa('Luiz Otavio' , 22, 'masculino')
pessoa3 = Pessoa('Nicolas', 27, 'masculino')
pessoa4 = Pessoa('Raquel', 53, 'feminino')

print(f'A primeira pessoa cadastrada se chama {pessoa1.nome}, tem {pessoa1.idade} anos de idade e é do sexo {pessoa1.sexo}')
print(f'A segunda pessoa cadastrada se chama {pessoa2.nome}, tem {pessoa2.idade} anos de idade e é do sexo {pessoa2.sexo}')
print(f'A terceira pessoa cadastrada se chama {pessoa3.nome}, tem {pessoa3.idade} anos de idade e é do sexo {pessoa3.sexo}')
print(f'A quarta pessoa cadastrada se chama {pessoa4.nome}, tem {pessoa4.idade} anos de idade e é do sexo {pessoa4.sexo}')
