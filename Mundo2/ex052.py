# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}

def num_primo(n: int) -> str:
    if n < 2:
        return f"{cores['negritoazul']}{n} NÃO é um Número Primo{cores['limpa']}"

    if n == 2:
        return f"{cores['negritoazul']}{n} é um Número Primo{cores['limpa']}"

    if n % 2 == 0:
        return f"{cores['negritoazul']}{n} NÃO é um Número Primo{cores['limpa']}"

    for num in range(3, int(n ** 0.5) + 1, 2): # Testa apenas números ímpares
        if n % num == 0:
            return f"{cores['negritoazul']}{n} NÃO é um Número Primo{cores['limpa']}"

    return f"{cores['negritoazul']}{n} é um Número Primo{cores['limpa']}"


# Passo 1: Receber um valor para "número"
n = int(input(f"{cores['pretoebranco']}Digite um número inteiro:{cores['limpa']} "))

# Passo 2: Exibir se é um número primo
print(num_primo(n))
# ----------------| Desafio [052]
