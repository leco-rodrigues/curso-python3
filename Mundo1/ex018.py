# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan


# Passo 1: Receber um valor para "ângulo"
angulo = float(input('\033[7;40mDigite um ângulo:\033[m '))

# Passo 2: Exibir o seno, cosseno e tangente
print(
      f'\033[1;34mO seno de um ângulo de {angulo}° é {sin(radians(angulo)):.2f}.\n'
      f'O cosseno de um ângulo de {angulo}° é {cos(radians(angulo)):.2f}.\n'
      f'A tangente de um ângulo de {angulo}° é {tan(radians(angulo)):.2f}.\033[m'
      )
# -------------------------------------------------------------------------------| Desafio [018]
