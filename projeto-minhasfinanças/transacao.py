from dataclasses import dataclass
from categoria import Categoria

@dataclass
class Transacao:
    descrição: str
    valor: float
    categoria: Categoria

    def exibir(self):
        print(f'DESCRIÇÃO: {self.descrição} | VALOR: {self.valor} | CATEGORIA: {self.categoria.nome}')