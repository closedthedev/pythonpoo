
class Musica: #criação da classe music
    
    def __init__(self, nome, artista, duracao): #método especial de inicialização (__init__) que é executado ao criar uma nova instância da classe
       
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

nova_musica = Musica('Sex, Drugs e etc', 'Beach Weather', 3.16)


print("Nome da música:", nova_musica.nome)  
print("Artista:", nova_musica.artista)     
print("Duração:", nova_musica.duracao)     