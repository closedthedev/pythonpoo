from dataclasses import dataclass


@dataclass
class Carro:

    modelo: str
    marca: str
    cor: str

carro1 = Carro('Renegade' , 'Jeep' , 'Preto')
carro2 = Carro('Gol', 'Volkswagen', 'Branco')
carro3 = Carro('Chevette', 'Chevrolet', 'Grafite')
print(f'O modelo do primero carro é {carro1.modelo}, da marca {carro1.marca} na cor {carro1.cor}')
print(f'O modelo do segundo carro é {carro2.modelo}, da marca {carro2.marca} na cor {carro1.cor}')
print(f'O modelo do terceiro carro é {carro3.modelo}, da marca {carro1.marca} na cor {carro1.cor}')
