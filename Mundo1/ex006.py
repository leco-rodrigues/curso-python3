# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# Passo 1: Receber um valor para "número"
n = float(input('\033[7;40mDigite um número:\033[m ')) # número

# Passo 2: Calcular e exibir a multiplicação e a raiz quadrada
print(f'\033[1;34mO dobro de {n} é igual a {n * 2}.\n' # dobro = n * 2
      f'O triplo de {n} é igual a {n * 3}.\n' # triplo = n * 3
      f'A raiz quadrada de {n} é igual a {n ** (1/2)}.\033[m') # raiz quadrada = n ** (1/2)
# -----------------------------------------------------------| Desafio [006]
