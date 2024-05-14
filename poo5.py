from dataclasses import dataclass


@dataclass
class Trabalho:
    cargo: str
    salario: float
    horas_semana: int

trabalho1 = Trabalho('Auxiliar de serviços gerais', 1164, 53)
trabalho2 = Trabalho('Montador Óptico', 1700, 50)


print(f'No meu primeiro trabalho, o meu cargo era {trabalho1.cargo}, eu recebia {trabalho1.salario} e trabalhava {trabalho1.horas_semana}h por semana')
print(f'No meu segundo trabalho, o meu cargo era {trabalho2.cargo}, eu recebia {trabalho2.salario} e trabalhava {trabalho2.horas_semana}h por semana')
