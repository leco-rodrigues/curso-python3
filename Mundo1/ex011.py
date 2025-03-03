# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m', 'negritoazul':'\033[1;34m'}

# Passo 1: Receber valores para "largura" e "altura"
largura = float(input(f"{cores['pretoebranco']}Qual a largura, em metros, da parede?{cores['limpa']} "))
altura = float(input(f"{cores['pretoebranco']}Qual a altura, em metros, da parede?{cores['limpa']} "))
print(f"{cores['negritoroxo']}Sua parede tem {altura} m de altura e {largura} m de largura.{cores['limpa']}")

# Passo 2: Exibir a área e a quantidade de tinta necessária
area = largura * altura
print(
      f"{cores['negritoazul']}A área é de {area} m².\n"

# Passo 3: Exibir a quantidade de tinta necessária
      f"Serão necessários {(area / 2)} l de tinta para pintá-la.{cores['limpa']}"
      )
# -------------------------------------------------------------------------------| Desafio [011]
