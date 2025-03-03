# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}

# Passo 1: Receber valores para três "números"
n1 = float(input(f"{cores['pretoebranco']}Digite o primeiro número:{cores['limpa']} "))
n2 = float(input(f"{cores['pretoebranco']}Digite o segundo número:{cores['limpa']} "))
n3 = float(input(f"{cores['pretoebranco']}Digite o terceiro número:{cores['limpa']} "))

# Passo 2: Exibir o maior número
if n2 < n1 > n3:
    print(f"{cores['negritoazul']}O maior número é o primeiro: {n1}{cores['limpa']}")
elif n1 < n2 > n3:
    print(f"{cores['negritoazul']}O maior número é o segundo: {n2}{cores['limpa']}")
elif n1 < n3 > n2:
    print(f"{cores['negritoazul']}O maior número é o terceiro: {n3}")
else:
    print(f"{cores['negritoazul']}Não há um único número maior ou todos são iguais.{cores['limpa']}")

# Passo 3: Exibir o menor número
if n2 > n1 < n3:
    print(f"{cores['negritoazul']}O menor número é o primeiro: {n1}{cores['limpa']}")
elif n1 > n2 < n3:
    print(f"{cores['negritoazul']}O menor número é o segundo: {n2}{cores['limpa']}")
elif n1 > n3 < n2:
    print(f"{cores['negritoazul']}O menor número é o terceiro: {n3}{cores['limpa']}")
else:
    print(f"{cores['negritoazul']}Não há um único número menor ou todos são iguais.{cores['limpa']}")
# --------------------------------------------------------------------------------------------------| Desafio [033]
