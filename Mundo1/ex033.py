# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Passo 1: Receber três valores para "três números"
n1 = float(input('Digite o primeiro número: ')) # primeiro número
n2 = float(input('Digite o segundo número: ')) # segundo número
n3 = float(input('Digite o terceiro número: ')) # terceiro número

# Passo 2: Criar uma condição composta para descobrir qual é o número maior
if n2 < n1 > n3:
    print(f'O maior é o primeiro número, {n1}!')
elif n1 < n2 > n3:
    print(f'O maior é o segundo número, {n2}!')
elif n1 < n3 > n2:
    print(f'O maior é o terceiro número, {n3}!')
else:
    print('Não há um único número maior ou são todos iguais!')
# ------------------------------------------------------------ Desafio [033]
