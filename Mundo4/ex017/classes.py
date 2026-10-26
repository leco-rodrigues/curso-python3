class Numero:
    def __init__(self, valor: int | float = 0) -> None:
        self.valor = valor

    def dobrar(self) -> None:
        self.valor = self.valor * 2

    def __str__(self) -> str:
        return f"Tenho o valor {self.valor} dentro do Número"

class Texto:
    def __init__(self, txt: str = "") -> None:
        self.texto = txt

    def dobrar(self) -> None:
        self.texto = self.texto + " " + self.texto

    def __str__(self) -> str:
        return f"Tenho o texto '{self.texto}' dentro do Texto"

class Lista:
    def __init__(self, lst: list[object] = []) -> None:
        self.valores = lst

    def dobrar(self) -> None:
        self.valores = self.valores + self.valores

    def __str__(self) -> str:
        return f"Tenho os valores {self.valores} dentro da Lista"

class Papel:
    def __init__(self) -> None:
        self.dobrado = False

    def dobrar(self) -> None:
        self.dobrado = True

    def __str__(self) -> str:
        return f"O papel está dobrado {'novo' if not self.dobrado else 'dobrado'}"

class Casa:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return f"Era uma casa muito engraçada..."

# DUCK TYPING
def tente_dobrar(objeto: object) -> None:
    try:
        objeto.dobrar()
    except:
        print(f"Tive dificuldades para dobrar {objeto.__class__.__name__}")
