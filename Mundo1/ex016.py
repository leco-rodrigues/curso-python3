from math import trunc


# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
    # Ex: Digite um número: 6.127
    #     O número 6.127 tem a parte Inteira 6.

# Passo 1: Receber um valor para "número Real"
n_real = float(input('Digite um número decimal: ')) # número real

# Passo 2: Mostrar a parte inteira
print(f'O número {n_real:.2f} tem a parte inteira igual a {trunc(n_real)}.') # parte inteira
# -------------------------------------------------------------------------- Desafio [016]
