# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

# Passo 1: Receber um valor para "número"
n = int(input('\033[7;40mDigite um número inteiro para fazer a tabuada:\033[m '))

# Passo 2: Exibir a tabuada
print(
      f'\033[1;34m{n} x  1 = {n * 1}\n'
      f'{n} x  2 = {n * 2}\n'
      f'{n} x  3 = {n * 3}\n'
      f'{n} x  4 = {n * 4}\n'
      f'{n} x  5 = {n * 5}\n'
      f'{n} x  6 = {n * 6}\n'
      f'{n} x  7 = {n * 7}\n'
      f'{n} x  8 = {n * 8}\n'
      f'{n} x  9 = {n * 9}\n'
      f'{n} x 10 = {n * 10}\033[m'
      )
# --------------------------------| Desafio [009]
