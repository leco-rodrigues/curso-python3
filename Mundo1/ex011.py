# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

# Passo 1: Receber os valores para "largura" e "altura"
l = float(input('Qual a largura da parede? ')) # largura
a = float(input('Qual a altura da parede? ')) # altura
print(f'Sua parede tem {a} metros de altura e {l} metros de largura.')

# Passo 2: Calcular a área e a quantidade de tinta
area = l * a
print(f'A área é igual a {area}m².' # área = largura * altura
      f'Será(ão) necessário(s) {(area / 2)}l de tinta para pintá-la.') # litros de tinta = largura * altura / 2
# -------------------------------------------------------------------- Desafio [011]
