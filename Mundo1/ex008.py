# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Passo 1: Receber um valor para "metros"
m = float(input(f'\033[7;40mDigite uma distância em metros:\033[m ')) # metros

# Passo 2: Converter e exibir em "centímetros" e "milímetros"
print(f'\033[1;34m{m} metros equivalem a {m * 100} centímetros.\n' # cm = m * 100
      f'{m} metros equivalem a {m * 1000} milímetros.\n' # mm = m * 1000

    # Extra: Quilômetros, hectômetros, decâmetros e decímetros
      f'{m} metros equivalem a {m / 1000} quilômetros.\n' # km = m / 1000
      f'{m} metros equivalem a {m / 100} hectômetros.\n' # hm = m / 100
      f'{m} metros equivalem a {m / 10} decâmetros.\n' # dam = m / 10
      f'{m} metros equivalem a {m * 10} decímetros.\033[m') # dm = m * 10
# --------------------------------------------------------| Desafio [008]
