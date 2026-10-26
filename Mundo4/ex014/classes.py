from functools import singledispatchmethod


class Analisador:
    @singledispatchmethod
    def analisar(self, valor) -> None:
        print(f"Não foi possível analisar o valor {valor}")

    @analisar.register
    def _(self, valor: int) -> None:
        print(f"{valor} é um número Inteiro")

    @analisar.register
    def _(self, valor: float) -> None:
        print(f"{valor} é um número com ponto flutuante (Real)")

    @analisar.register
    def _(self, valor: str) -> None:
        print(f"'{valor}' é uma cadeia de caracteres")

    @analisar.register
    def _(self, valor: tuple | list | dict) -> None:
        print(f"{valor} é uma coleção de dados")
