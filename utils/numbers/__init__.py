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

def resumo(n: float, a: float, d: float) -> None:
    n_dobro: float = dobro(n)
    n_metade: float = metade(n)
    n_aumento: float = aumentar(n, a)
    n_desconto: float = diminuir(n, d)
    
    print("-" * 25 + "\n     RESUMO DO VALOR\n" + "-" * 25)
    print(f"Valor:           {moeda(n)}")
    print(f"Dobro:           {n_dobro}")
    print(f"Metade:          {n_metade}")
    print(f"Aumento de {a}%:  {n_aumento}")
    print(f"Desconto de {d}%: {n_desconto}")
    print("-" * 25)
