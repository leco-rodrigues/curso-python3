# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m'}
# Passo 1: Receber valores para três "números"
n1 = float(input(f'{cores['pretoebranco']}Digite o primeiro número:{cores['limpa']} ')) # primeiro número
n2 = float(input(f'{cores['pretoebranco']}Digite o segundo número:{cores['limpa']} ')) # segundo número
n3 = float(input(f'{cores['pretoebranco']}Digite o terceiro número:{cores['limpa']} ')) # terceiro número

# Passo 2: Criar uma condição composta para descobrir qual é o número maior e qual é o menor
    # Número maior
if n2 < n1 > n3:
    print(f'{cores['negritoroxo']}O maior número é o primeiro: {n1}{cores['limpa']}')
elif n1 < n2 > n3:
    print(f'{cores['negritoroxo']}O maior número é o segundo: {n2}{cores['limpa']}')
elif n1 < n3 > n2:
    print(f'{cores['negritoroxo']}O maior número é o terceiro: {n3}')
else:
    print(f'{cores['negritoroxo']}Não há um único número maior ou todos são iguais.{cores['limpa']}')

    # Número menor
if n2 > n1 < n3:
    print(f'{cores['negritoroxo']}O menor número é o primeiro: {n1}{cores['limpa']}')
elif n1 > n2 < n3:
    print(f'{cores['negritoroxo']}O menor número é o segundo: {n2}{cores['limpa']}')
elif n1 > n3 < n2:
    print(f'{cores['negritoroxo']}O menor número é o terceiro: {n3}{cores['limpa']}')
else:
    print(f'{cores['negritoroxo']}Não há um único número menor ou todos são iguais.{cores['limpa']}')
# --------------------------------------------------------------------------------------------------| Desafio [033]
