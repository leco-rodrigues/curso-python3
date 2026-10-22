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


def e_numero(valor: object) -> bool:
    if isinstance(valor, int) or isinstance(valor, float):
        return True
    return False

def numero_positivo(valor: float) -> bool:
    if 0 < valor:
        return True
    return False


# Passo 1: Criar classe Retangulo
class Retangulo:
    def __init__(self, base: float = 1, altura: float = 1) -> None:
        if e_numero(base) and e_numero(altura):
            if numero_positivo(base) and numero_positivo(altura):
                self._base = base
                self._altura = altura
            else:
                raise ValueError("Valores negativos são inválidos")
        else:
            raise TypeError("Valores não numéricos são inválidos")
        self._area: float | None = None

    @property
    def base(self) -> float:
        return self._base

    @base.setter
    def base(self, valor: float) -> None:
        if e_numero(valor):
            if numero_positivo(valor):
                self._base = valor
            else:
                raise ValueError("Valor inválido para a base")
        else:
            raise TypeError("O valor da base deve ser um número")

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, valor: float) -> None:
        if e_numero(valor):
            if numero_positivo(valor):
                self._altura = valor
            else:
                raise ValueError("Valor inválido para a altura")
        else:
            raise TypeError("O valor da altura deve ser um número")

    @property
    def area(self) -> float:
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self) -> None:
        raise PermissionError("Área não pode ser configurada desse jeito.")

    @property
    def medidas(self) -> str:
        medidas: str = f"Base = {self._base}\nAltura = {self._altura}\nÁrea = {self.area}"
        return medidas

    @medidas.setter
    def medidas(self, medidas: tuple[float]) -> None:
        if len(medidas) == 2:
            if isinstance(medidas[0], int) or isinstance(medidas[0], float):
                if numero_positivo(medidas[0]):
                    self._base = medidas[0]
                else:
                    raise ValueError("Valor inválido para a base")
            else:
                raise TypeError("O valor da base deve ser um número")
            if isinstance(medidas[1], int) or isinstance(medidas[1], float):
                if numero_positivo(medidas[1]):
                        self._altura = medidas[1]
                else:
                    raise ValueError("Valor inválido para altura")
            else:
                raise TypeError("O valor da altura deve ser um número")
        else:
            raise ValueError("Por favor, informe as medidas de base e altura do retângulo dentro de uma tupla")

# Passo 2: Exibir o resultado
r: Retangulo = Retangulo(3, 4)
r.base = 12
r.altura = 33
# r.base = -12
# r.altura = -33
r.medidas = (9, 3)
# r.medidas = (9, 3, 1)

print(r.medidas)
inspect(r, private=True, methods=True)
# -| AULA 12 - DOMINE ENCAPSULAMENTO EM PYTHON COM GETTERS, SETTERS E 6 PROJETOS REAIS | DESAFIO 31
