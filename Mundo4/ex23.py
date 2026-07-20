# Exercício de polígonos:
    # Implemente o seguinte diagrama de classes:
        # Poligono (abstract) + qtd_lados + perimetro() (abstract) + area() (abstract)
        # Quadrado(Poligono) + lado + perimetro() + area()
        # Circulo(Poligono) + raio + perimetro() + area()

from abc import ABC, abstractmethod

# Passo 1: Criar classe abstrata Poligono
class Poligono(ABC):
    def __init__(self, qtd_lados: int) -> None:
        self.qtd_lados = qtd_lados

# Passo 2: Criar método abstrato perimetro()
    @abstractmethod
    def perimetro(self) -> None:
        pass

# Passo 3: Criar método abstrato area()
    @abstractmethod
    def area(self) -> None:
        pass

# Passo 4: Criar subclasse Quadrado
class Quadrado(Poligono):
    def __init__(self, qtd_lados: int, lado: float) -> None:
        super().__init__(qtd_lados)
        self.lado = lado

    def perimetro(self) -> None:
        valor_perimetro: float = 4 * self.lado
        print(f"O perímetro do quadrado é igual a {valor_perimetro}.")

    def area(self) -> None:
        valor_area: float = self.lado * self.lado
        print(f"A área do quadrado é igual a {valor_area}.")

# Passo 5: Criar subclasse Circulo
class Circulo(Poligono):
    def __init__(self, qtd_lados: int, raio: float) -> None:
        super().__init__(qtd_lados)
        self.raio = raio

    def perimetro(self) -> None:
        PI: float = 3.14
        valor_perimetro: float = 2 * PI * self.raio
        print(f"O perímetro do círculo é igual a {valor_perimetro:.1f}.")

    def area(self) -> None:
        PI: float = 3.14
        valor_area: float = PI * (self.raio * self.raio)
        print(f"A área do círculo é igual a {valor_area:.1f}.")

# Passo 6: Exibir o resultado
q1: Circulo = Circulo(4, 20)
q1.perimetro()
q1.area()

# -| AULA 09 - DESAFIOS DE HERANÇA, ABSTRAÇÃO E CLASSES | DESAFIO 23
