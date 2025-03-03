# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

from math import sqrt


# Passo 1: Receber valores para "cateto oposto" e "cateto adjacente"
cateto_o = float(input('\033[7;40mQual o comprimento do cateto oposto?\033[m '))
cateto_a = float(input('\033[7;40mQual o comprimento do cateto adjacente?\033[m '))

# Passo 2: Exibir o comprimento da hipotenusa
print(f'\033[1;34mO comprimento da hipotenusa é de {sqrt(cateto_o ** 2 + cateto_a ** 2):.2f}.\033[m')
# --------------------------------------------------------------------------------------------------| Desafio [017]
