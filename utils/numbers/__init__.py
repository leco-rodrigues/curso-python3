def dobro(n: float, format: bool = True) -> float:
    n = n * 2
    if(format):
       n = moeda(n)
    return n

def metade(n: float, format: bool = True) -> float:
    n = n / 2
    if(format):
        n = moeda(n)
    return n

def aumentar(n: float, p: float, format: bool = True) -> float:
    n = n * (1 + (p / 100))
    if(format):
        n = moeda(n)
    return n

def diminuir(n: float, p: float, format: bool = True) -> float:
    n = n * (1 - (p / 100))
    if(format):
        n = moeda(n)
    return n

def moeda(n: float) -> str:
    return f"R${n:.2f}".replace(".", ",")
