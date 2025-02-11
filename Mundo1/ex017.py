from math import sqrt


# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}
# Passo 1: Receber valores para "cateto oposto" e "cateto adjacente"
cateto_o = float(input(f'{cores['pretoebranco']}Qual o comprimento do cateto oposto?{cores['limpa']} ')) # cateto oposto
cateto_a = float(input(f'{cores['pretoebranco']}Qual o comprimento do cateto adjacente?{cores['limpa']} ')) # cateto adjacente

# Passo 2: Calcular e exibir o comprimento da hipotenusa
print(f'{cores['negritoazul']}O comprimento da hipotenusa é de {sqrt(cateto_o ** 2 + cateto_a ** 2):.2f} metros.{cores['limpa']}') # hipotenusa = (cateto oposto ** 2 + cateto adjacente ** 2) ** (1/2)
# -------------------------------------------------------------------------------------------------------------------------------| Desafio [017]
