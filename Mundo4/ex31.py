# Retângulo:
    # Crie uma classe que represente um retângulo plas syas medidas e área.
        # classe Retangulo
        # _base
        # _altura
        # _area
        # @base
        # @altura
        # @medidas
        # @area
from rich import print, inspect


def numero_positivo(valor: float) -> bool:
    if 0 < valor:
        return True
    return False


# Passo 1: Criar classe Retangulo
class Retangulo:
    def __init__(self, base: float = 1, altura: float = 1) -> None:
        if numero_positivo(base) and numero_positivo(altura):
            self._base = base
            self._altura = altura
        else:
            raise ValueError("Valores negativos são inválidos")
        self._area: None = None

    @property
    def base(self) -> float:
        return self._base

    @base.setter
    def base(self, valor: float) -> None:
        if numero_positivo(valor):
            self._base = valor
        else:
            raise ValueError("Valor inválido para a base")

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, valor: float) -> None:
        if numero_positivo(valor):
            self._altura = valor
        else:
            raise ValueError("Valor inválido para a altura")

    @property
    def area(self) -> float:
        return self._base * self._altura

    @area.setter
    def area(self) -> None:
        raise TypeError

    @property
    def medidas(self) -> str:
        medidas: str = f"Base = {self._base}\nAltura = {self._altura}\nÁrea = {self._area}"
        return medidas

    @medidas.setter
    def medidas(self, medidas: tuple[float]) -> None:
        if numero_positivo(medidas[0]):
            self._base = medidas[0]
        else:
            raise ValueError("Valor inválido para a base")
        if numero_positivo(medidas[1]):
                self._altura = medidas[1]
        else:
            raise ValueError("Valor inválido para altura")

# Passo 2: Exibir o resultado
r: Retangulo = Retangulo()
r.base = 12
r.altura = 33
r.medidas = (9, 3)

print(r.medidas)
inspect(r, private=True, methods=True)
# -| AULA 12 - DOMINE ENCAPSULAMENTO EM PYTHON COM GETTERS, SETTERS E 6 PROJETOS REAIS | DESAFIO 31
