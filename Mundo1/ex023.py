# Faça um programa que leia im número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
    # Ex: Digite um número: 1834
    #     unidade: 4
    #     dezena: 3
    #     centena: 8
    #     milhar: 1

# Passo 1: Receber um valor para "número"
n = input('Digite um número de 0 a 9999: ') # número

# Passo 2: Separar cada um dos dígitos em unidade, dezena, centena e milhar
print(f'''Classificando cada um dos dígitos:
      unidade: {n[-1]}
      dezena: {n[-2]}
      centena: {n[-3]}
      milhar: {n[-4]}''')
# ----------------------- Desafio [023]
