from math import sin, cos, tan, radians


# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Passo 1: Receber um valor de "ângulo"
angulo = float(input('Digite um ângulo: '))

# Passo 2: Calcular o "seno", "cosseno" e "tangente" com base nesse valor
print(f'O seno de um ângulo de {angulo}° é {sin(radians(angulo)):.2f}.')
print(f'O cosseno de um ângulo de {angulo}° é {cos(radians(angulo)):.2f}.')
print(f'A tangente de um ângulo de {angulo}° é {tan(radians(angulo)):.2f}.')
# -------------------------------------------------------------------------- Desafio [018]
