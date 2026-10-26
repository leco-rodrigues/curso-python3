class Carteira:
    def __init__(self, valor: int | float = 0) -> None:
        self.__saldo = valor

    def __str__(self) -> str:
        return f"Você tem R${self.saldo:,.2f} na carteira"

    @property
    def saldo(self) -> int | float:
        return self.__saldo

    @saldo.setter
    def saldo(self, valor: int | float) -> None:
        raise PermissionError("Você não tem autorização para alterar o saldo desse jeito")

    def __eq__(self, outro: Carteira) -> bool:
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False

    def __iadd__(self, valor: int | float) -> Carteira:
        self.__saldo = self.__saldo + valor
        return self

    def __isub__(self, valor: int | float) -> Carteira:
        self.__saldo = self.__saldo - valor
        return self

    def __lt__(self, outro: Carteira) -> bool:
        if self.__saldo < outro.__saldo:
            return True
        else:
            return False
