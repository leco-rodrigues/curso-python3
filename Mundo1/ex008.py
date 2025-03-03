# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Passo 1: Receber um valor para "metros"
m = int(input('\033[7;40mDigite uma distância em metros:\033[m '))

# Passo 2: Exibir em centímetros e milímetros
print(
      f'\033[1;34m{m} m equivalem a {m * 100} cm (centímetros).\n'
      f'{m} m equivalem a {m * 1000} mm (milímetros).\n'
    # Extra: Quilômetros, hectômetros, decâmetros e decímetros
      f'{m} m equivalem a {m / 1000} km (quilômetro).\n'
      f'{m} m equivalem a {m / 100} hm (hectômetro).\n'
      f'{m} m equivalem a {m / 10} dam (decâmetro).\n'
      f'{m} m equivalem a {m * 10} dm (decímetro).\033[m'
      )
# -------------------------------------------------------| Desafio [008]
