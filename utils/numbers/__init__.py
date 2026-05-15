def dobro(n: float) -> float:
    return n * 2

def metade(n: float) -> float:
    return n / 2

def aumentar(n: float, p: float) -> float:
    return n * (1 + (p / 100))

def diminuir(n: float, p: float) -> float:
    return n * (1 - (p / 100))

def moeda(n: float) -> str:
    return f"R${n:.2f}"
