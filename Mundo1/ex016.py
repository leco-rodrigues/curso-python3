from math import trunc


# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
    # Ex: Digite um número: 6.127
    #     O número 6.127 tem a parte Inteira 6.

# Passo 1: Receber um valor de "número Real"
num_real = float(input('Digite um número decimal: '))

# Passo 2: Mostrar apenas a parte inteira desse valor
print(f'O número {num_real:.2f} tem a parte inteira igual a {trunc(num_real)}.')
# ------------------------------------------------------------------------------ Desafio [016]
