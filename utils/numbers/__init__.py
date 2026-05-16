def dobro(n: float, format: bool = False) -> float:
    n = n * 2
    if(format):
       n = moeda(n)
    return n

def metade(n: float, format: bool = False) -> float:
    n = n / 2
    if(format):
        n = moeda(n)
    return n

def aumentar(n: float, p: float, format: bool = False) -> float:
    n = n * (1 + (p / 100))
    if(format):
        n = moeda(n)
    return n

def diminuir(n: float, p: float, format: bool = False) -> float:
    n = n * (1 - (p / 100))
    if(format):
        n = moeda(n)
    return n

def moeda(n: float, m: str = "R$") -> str:
    return f"{m}{n:.2f}".replace(".", ",")

def resumo(n: float, a: float, d: float) -> None:
    n_dobro: float = dobro(n, True)
    n_metade: float = metade(n, True)
    n_aumento: float = aumentar(n, a, True)
    n_desconto: float = diminuir(n, d, True)
    
    print("-" * 25 + "\n     RESUMO DO VALOR\n" + "-" * 25)
    print(f"Valor:            {moeda(n)}")
    print(f"Dobro:            {n_dobro}")
    print(f"Metade:           {n_metade}")
    print(f"Aumento de {a}%:  {n_aumento}")
    print(f"Desconto de {d}%: {n_desconto}")
    print("-" * 25)

def leiaDinheiro(n: str = None) -> float:
    while True:
        n: str = input("Digite um valor: R$")
        n_formatted: str = n.replace(",", ".")

        if not(n_formatted.strip().replace(".", "").isdigit()):
            print(f"ERRO: '{n_formatted}' não é um valor monetário válido.")
            continue
        break
    n_formatted = float(n_formatted)
    return n_formatted
