# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
    # Ex: Digite um número: 6.127
    #     O número 6.127 tem a parte Inteira 6.

from math import trunc


# Passo 1: Receber um valor para "número"
n = float(input('\033[7;40mDigite um número decimal:\033[m '))

# Passo 2: Exibir a parte inteira
print(f'\033[1;34mO número {n} tem a parte inteira igual a {trunc(n)}.\033[m')
# ---------------------------------------------------------------------------| Desafio [016]
