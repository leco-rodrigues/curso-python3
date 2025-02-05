from math import sqrt


# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

# Passo 1: Receber os valores de "cateto oposto" e "cateto adjacente"
cateto_o = float(input('Qual o comprimento do cateto oposto? '))
cateto_a = float(input('Qual o comprimento do cateto adjacente? '))

# Passo 2: Calcular o comprimento da hipotenusa com base nesses valores ((a² + b²) ** (1/2))
print(f'O comprimento da hipotenusa é {sqrt(cateto_o ** 2 + cateto_a ** 2):.2f} metros.')
# --------------------------------------------------------------------------------------- Desafio [017]
