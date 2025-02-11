# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}
# Passo 1: Receber valores para "largura" e "altura"
l = float(input(f'{cores['pretoebranco']}Qual a largura da parede?{cores['limpa']} ')) # largura
a = float(input(f'{cores['pretoebranco']}Qual a altura da parede?{cores['limpa']} ')) # altura
print(f'{cores['negritoazul']}Sua parede tem {a}m de altura e {l}m de largura.{cores['limpa']}')

# Passo 2: Calcular e exibir a área e a quantidade de tinta necessária
area = l * a
print(f'{cores['negritoazul']}A área é igual a {area}m². ' # área = largura * altura
      f'Será(ão) necessário(s) {(area / 2)}l de tinta para pintá-la.{cores['limpa']}') # litros de tinta = largura * altura / 2
# -----------------------------------------------------------------------------------| Desafio [011]
