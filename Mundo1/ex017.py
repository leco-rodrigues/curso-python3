from math import sqrt


# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

# Passo 1: Receber os valores para "cateto oposto" e "cateto adjacente"
cateto_o = float(input('Qual o comprimento do cateto oposto? ')) # cateto oposto
cateto_a = float(input('Qual o comprimento do cateto adjacente? ')) # cateto adjacente

# Passo 2: Calcular o comprimento da hipotenusa
print(f'O comprimento da hipotenusa é {sqrt(cateto_o ** 2 + cateto_a ** 2):.2f} metros.') # hipotenusa = (cateto oposto ** 2 + cateto adjacente ** 2) ** (1/2)
# --------------------------------------------------------------------------------------- Desafio [017]
