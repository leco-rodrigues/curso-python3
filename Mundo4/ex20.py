# Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa.
# Crie também um método que permita mostrar a ficha desse gamer.

from rich import print
from rich.panel import Panel

# Passo 1: Criar classe Gamer
class Gamer:
    def __init__(self, nome: str, nick: str):
        self.nome = nome
        self.nick = nick
        self.favoritos: list[str] = []

# Passo 2: Criar método para adicionar os jogos favoritos
    def add_favoritos(self, jogo: str):
        self.favoritos.append(f":video_game: {jogo}")

# Passo 3: Criar método para mostrar a ficha
    def ficha(self):
        panel_conteudo: str = "\n".join(sorted(self.favoritos))

        print(Panel(f"""
Nome real: [black on blue]{self.nome}[/]
Jogos favoritos:
{panel_conteudo}
                    """, title = f"Jogador <{self.nick}>", width = 40))

# Passo 4: Exibir o resultado
j1 = Gamer("Fabricio da Silva", "detonator2025")
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortinite")
j1.ficha()

# -| AULA 06 - APRENDA PROGRAMAÇÃO ORIENTADA A OBJETOS COM DESAFIOS EM PYTHON | DESAFIO 20
