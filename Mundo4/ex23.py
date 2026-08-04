# Exercício de polígonos:
    # Implemente o seguinte diagrama de classes:
        # Poligono (abstract) + qtd_lados + perimetro() (abstract) + area() (abstract)
        # Quadrado(Poligono) + lado + perimetro() + area()
        # Circulo(Poligono) + raio + perimetro() + area()

from abc import ABC, abstractmethod
from math import pi


# Passo 1: Criar classe abstrata Poligono
class Poligono(ABC):

    def __init__(self, qtd_lados: int) -> None:
        self.qtd_lados = qtd_lados

# Passo 2: Criar método abstrato perimetro()
    @abstractmethod
    def perimetro(self) -> float:
        pass

# Passo 3: Criar método abstrato area()
    @abstractmethod
    def area(self) -> float:
        pass

# Passo 4: Criar subclasse Quadrado
class Quadrado(Poligono):

    def __init__(self, lado: int = 1) -> None:
        super().__init__(4)
        self.lado = lado

    def perimetro(self) -> float:
        return self.lado * 4

    def area(self) -> float:
        return self.lado ** 2

# Passo 5: Criar subclasse Circulo
class Circulo(Poligono):

    def __init__(self, raio: float = 1) -> None:
        super().__init__(0)
        self.raio = raio

    def perimetro(self) -> float:
        return 2 * pi * self.raio

    def area(self) -> float:
        return pi * self.raio ** 2

# Passo 6: Exibir o resultado
q: Quadrado = Quadrado(20)

print(f"Perímetro = {q.perimetro():.1f}mm")
print(f"Área = {q.area():.1f}mm²")

c: Circulo = Circulo(12)

print(f"Perímetro = {c.perimetro():.1f}cm")
print(f"Área = {c.area():.1f}cm²")

# -| AULA 09 - DESAFIOS DE HERANÇA, ABSTRAÇÃO E CLASSES | DESAFIO 23
