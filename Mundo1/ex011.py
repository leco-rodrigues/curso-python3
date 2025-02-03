# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

# Passo 1: Receber um valor de "metros"
base = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
print(f'Base: {base} metros. Altura: {altura} metros.')

# Passo 2: Calcular a área desse valor (base x altura)
area = base * altura
print(f'A área dessa parede é igual a {area}m.')

# Passo 3: Calcular a quatidade de tinta necessária para pintá-la (area / 2)
print(f'Será(ão) necessário(s) {(area / 2) * (1/4)}l de tinta para pintá-la.')
# ---------------------------------------------------------------------------- Desafio [011]
