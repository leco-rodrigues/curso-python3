# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Passo 1: Receber um valor para "metros"
m = float(input('Digite uma distância em metros: ')) # metros

# Passo 2: Converter em "centímetros" e "milímetros"
print(f'{m} metros equivalem a {m * 100} centímetros.\n' # cm = m * 100
      f'{m} metros equivalem a {m * 1000} milímetros.\n' # mm = m * 1000

    # Extra: Converter em quilômetros (km), hectômetros (hm), decâmetros (dam) e decímetros (dm).
      f'{m} metros equivalem a {m / 1000} quilômetros.\n' # km = m / 1000
      f'{m} metros equivalem a {m / 100} hectômetros.\n' # hm = m / 100
      f'{m} metros equivalem a {m / 10} decâmetros.\n' # dam = m / 10
      f'{m} metros equivalem a {m * 10} decímetros.') # dm = m * 10
# --------------------------------------------------- Desafio [008]
