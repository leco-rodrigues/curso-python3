# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

# Passo 1: Receber um valor para "número"
n = int(input('\033[7;40mDigite um número:\033[m ')) # número

# Passo 2: Calcular e exibir o antecessor e o sucessor
print(f'\033[1;34mO antecessor de {n} é {n - 1}.\n' # antecessor = n - 1
      f'E seu sucessor é {n + 1}.\033[m') # sucessor = n + 1
# --------------------------------------| Desafio [005]
