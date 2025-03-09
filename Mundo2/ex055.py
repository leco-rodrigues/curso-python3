# Faça um programa que leia o peso de cinco pessoas. No final, motre qual foi o maior e o menor peso lidos.

# Passo 1: Receber cinco valores para "pesos"
pesos: list[float] = []
for pessoa in range(1, 6):
    peso:float = input(f'\033[7;40mPeso (kg) da {pessoa}° pessoa:\033[m ')
    pesos.append(peso)

# Passo 2: Exibir o maior peso
print(f'\033[1;34mO maior peso é {max(pesos)} kg.\033[m')

# Passo 3: Exibir o menor peso
print(f'\033[1;34mO menor peso é {min(pesos)} kg.\033[m')
# ------------------------------------------------------| Desafio [055]
