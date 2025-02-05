from math import sin, cos, tan, radians


# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Passo 1: Receber um valor para "ângulo"
ang = float(input('Digite um ângulo: ')) # ângulo

# Passo 2: Calcular o "seno", "cosseno" e "tangente"
print(f'O seno de um ângulo de {ang}° é {sin(radians(ang)):.2f}.\n' # seno 
      f'O cosseno de um ângulo de {ang}° é {cos(radians(ang)):.2f}.\n' # cosseno 
      f'A tangente de um ângulo de {ang}° é {tan(radians(ang)):.2f}.') # tangente 
# -------------------------------------------------------------------- Desafio [018]
