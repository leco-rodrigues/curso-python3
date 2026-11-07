# Criando um Sistema de Pagamentos com Polimorfismo:
    # Crie um simulador que gerencie a pagamentos em diferentes tipos.
    # Pagamento(abstract)
    # # valor
    # + @fvalor
    # + pagar()
    # Boleto(Pagamento)
    # Pix(Pagamento)
    # Credito(Pagamento)
from abc import ABC, abstractmethod
from math import isfinite


def e_numero(valor: object) -> bool:
    if isinstance(valor, bool):
        return False
    if isinstance(valor, (int, float)) and isfinite(valor):
        return True
    return False

def numero_positivo(valor: object) -> bool:
    if e_numero(valor):
        if valor > 0:
            return True
        return False
    return False


translation = str.maketrans({",": ".", ".": ","})

# Passo 1: Criar classe Pagamento(abstract)
class Pagamento(ABC):
    def __init__(self, valor: int| float = 1) -> None:
        if numero_positivo(valor):
            self._valor = valor
        else:
            raise ValueError(f"'{valor}' não é um valor válido")

    @property
    def valor(self) -> int | float:
        return self._valor

    @valor.setter
    def valor(self, valor: int | float) -> None:
        if numero_positivo(valor):
            self._valor = valor
        else:
            raise ValueError(f"'{valor}' não é um valor válido")

    @property
    def fvalor(self) -> str:
        return f"R$ {self.valor:,.2f}".translate(translation)

# Passo 2: Criar método abstrato polimórfico pagar()
    @abstractmethod
    def pagar(self) -> None:
        pass

# Passo 3: Criar classe Boleto(Pagamento)
class Boleto(Pagamento):
    def pagar(self) -> None:
        print(f"Pagamento CONFIRMADO de {self.fvalor} via Boleto")

# Passo 4: Criar classe Pix(Pagamento)
class Pix(Pagamento):
    def pagar(self) -> None:
        print(f"Pagamento CONFIRMADO de {self.fvalor} via Pix")

# Passo 5: Criar classe CartaoCredito(Pagamento)
class CartaoCredito(Pagamento):
    def pagar(self) -> None:
        print(f"Pagamento CONFIRMADO de {self.fvalor} via Cartão de Crédito")

class Exemplo:
    def __init__(self) -> None:
        pass

# Passo 6: Criar método polimórfico finalizar_comprar():
def finalizar_compra(forma_pag: Pagamento, valor: int | float) -> None:
    if not isinstance(forma_pag, Pagamento):
        raise TypeError("A forma de pagamento deve ser um objeto Pagamento.")

    forma_pag.valor = valor
    forma_pag.pagar()

# Passo 7: Exibir o resultado
finalizar_compra(Pix(), 8_500)
finalizar_compra(CartaoCredito(), 8_500)
finalizar_compra(Boleto(), 8_500)
# finalizar_compra(Pix(), -100)
# finalizar_compra(Exemplo(), 1000)
# -| AULA 15 - 7 DESAFIOS DE POLIMORFISMO EM PTYHON | DESAFIO 36
