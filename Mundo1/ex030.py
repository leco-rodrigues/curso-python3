# Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou ÍMPAR.

# Passo 1: Receber um valor para "número inteiro"
n = int(input('Digite um número inteiro: ')) # número inteiro

# Passo 2: Criar uma condição composta para dizer se é par ou ímpar
if n % 2 == 0:
    print(f'{n} é PAR!')
else:
    print(f'{n} é ÍMPAR!')
# ------------------------ Desafio [030]
