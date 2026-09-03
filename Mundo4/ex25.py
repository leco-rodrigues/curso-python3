# Sistema de frete:
    # Crie classes capazes de calcular fretes de veículos diferentes
        # Transporte (abstract) + distancia + frete + calc_frete() (abstract)
        # Moto + fator = 0.5 + calc_frete()
        # Caminhao + fator = 1.20 + calc_frete()
        # Drone + fator = 9.5 + calc_frete()

from abc import ABC, abstractmethod
from rich import print
from rich.table import Table


# Passo 1: Criar classe abstrata Transporte
class Transporte(ABC):

    def __init__(self, distancia: float) -> None:
        self.distancia = distancia
        self.frete = 0

# Passo 2: Criar método abstrato calc_frete()
    @abstractmethod
    def calcular_frete(self) -> str:
        pass

# Passo 3: Criar classe Moto (livre)
class Moto(Transporte):
    fator: float = 0.50

    def __init__(self, distancia: float) -> None:
        super().__init__(distancia)

    def calcular_frete(self) -> str:
        self.frete = self.distancia * Moto.fator
        return f"R${self.frete:.2f}"

# Passo 4: Criar classe Caminhao (mínimo 50Km)
class Caminhao(Transporte):
    fator: float = 1.20

    def __init__(self, distancia: float) -> None:
        super().__init__(distancia)

    def calcular_frete(self) -> str:
        if self.distancia < 50:
            return f"Raio mínimo de 50Km"
        else:
            self.frete = self.distancia * Caminhao.fator
            return f"R${self.frete:.2f}"

# Passo 5: Criar classe Drone (máximo 10Km)
class Drone(Transporte):
    fator: float = 9.50

    def __init__(self, distancia: float) -> None:
        super().__init__(distancia)

    def calcular_frete(self) -> str:
        if self.distancia > 10:
            return f"Raio máximo de 10Km"
        else:
            self.frete = self.distancia * Drone.fator
            return f"R${self.frete:.2f}"


# Passo 6: Exibir o resultado
dist: float = 80

# entrega = Drone(dist)
# print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_frete()}")

viagem: list[object] = [Moto(dist), Caminhao(dist), Drone(dist)]

tabela: Table = Table(title = "Tabela de Fretes")
tabela.add_column("Distância")
tabela.add_column("Tipo")
tabela.add_column("Frete")

for item in viagem:
    tabela.add_row(f"{dist}Km", f"{type(item).__name__}", f"{item.calcular_frete()}")

print(tabela)

# -| AULA 09 - DESAFIOS DE HERANÇA, ABSTRAÇÃO E CLASSES | DESAFIO 25
