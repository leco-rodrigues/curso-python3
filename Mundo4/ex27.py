# Sistema de batalha de RPG:
    # Simule o sistema de batalha entre perosnagens de um RPG
        # Personagem (abstract) + nome + vida + golpes + atacar(alvo, força) + receber_dano(dano) + curar() (abstract)
        # Guerreiro + curar()
        # Mago + curar()

from abc import ABC, abstractmethod
from rich import print
from random import choice

# Passo 1: Criar classe abstrata Personagem
class Personagem(ABC):
    golpes: list[str]

    def __init__(self, nome: str, vida: float) -> None:
        self.nome = nome
        self.vida = vida

# Passo 2: Criar método atacar()
    def atacar(self, alvo: object, forca: float) -> None:
        dano: int = self.receber_dano(forca)
        print(f"""
[green]{self.nome}[/]([cyan]{self.vida}[/]) atacou [bold red]{getattr(alvo, 'nome')}[/]([cyan]{getattr(alvo, 'vida')}[/]) com um [blue]{choice(self.golpes)}[/] de força [cyan]{forca}[/]
[blue]{getattr(alvo, "nome")}[/] recebeu [red]dano de {dano}[/]!
                """)
        setattr(alvo, "vida", getattr(alvo, "vida") - dano)

# Passo 3: Criar método receber_dano()
    def receber_dano(self, dano: float) -> int:
        dano_final: int = choice([i for i in range(1, int(dano) + 1)])
        return dano_final

# Passo 4: Criar método abstrato curar()
    @abstractmethod
    def curar(self) -> None:
        pass

# Passo 5: Criar subclasse Guerreiro
class Guerreiro(Personagem):
    golpes: list[str] = ["Soco", "Pulo Giratório", "Golpe de Machado"]

    def __init__(self, nome: str, vida: float) -> None:
        super().__init__(nome, vida)

    def curar(self) -> None:
        cura: int = choice([i for i in range(1, 101)])
        self.vida += cura
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {cura} pontos[/] de vida.")

# Passo 6: Criar subclasse Mago
class Mago(Personagem):
    golpes: list[str] = ["Bola de Fogo", "Raio"]

    def __init__(self, nome: str, vida: float) -> None:
        super().__init__(nome, vida)

    def curar(self) -> None:
        cura: int = choice([i for i in range(1, 101)])
        self.vida += cura
        print(f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {cura} pontos[/] de vida.")

# Passo 7: Exibir o resultado
p1: Guerreiro = Guerreiro("Kratos", 2000)
p2: Mago = Mago("Merlin", 3000)

p1.atacar(p2, 1000)
p2.curar()
p2.atacar(p1, 20000)
p1.curar()

# -| AULA 09 - DESAFIOS DE HERANÇA, ABSTRAÇÃO E CLASSES | DESAFIO 27
