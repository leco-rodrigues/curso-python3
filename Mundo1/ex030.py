# Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou ÍMPAR.

# Passo 1: Receber um valor para "número"
n = int(input('\033[7;40mDigite um número inteiro:\033[m '))

# Passo 2: Exibir se é "par" ou "ímpar"
if n % 2 == 0:
    print(f'\033[1;34m{n} é PAR!\033[m')
else:
    print(f'\033[1;34m{n} é ÍMPAR!\033[m')
# ---------------------------------------| Desafio [030]
