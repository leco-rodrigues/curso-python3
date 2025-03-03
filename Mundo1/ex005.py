# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

# Passo 1: Receber um valor para "número"
n = int(input('\033[7;40mDigite um número inteiro:\033[m '))

# Passo 2: Exibir o antecessor
print(
      f'\033[1;34mO antecessor de {n} é {n - 1}.\n'

# Passo 3: Exibir o sucessor
      f'O sucessor de {n} é {n + 1}.\033[m'
      )
# -----------------------------------------| Desafio [005]
