# Faça um programa que leia im número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
    # Ex: Digite um número: 1834
    #     unidade: 4
    #     dezena: 3
    #     centena: 8
    #     milhar: 1

# Passo 1: Receber um valor para "número"
n = input('\033[7;40mDigite um número de 0 a 9999:\033[m ').replace(' ', '').zfill(4) # número

# Passo 2: Separar e exibir cada um dos dígitos em unidade, dezena, centena e milhar
print(f'''\033[1;34mClassificando cada um dos dígitos:
      unidade: {n[-1]}
      dezena: {n[-2]}
      centena: {n[-3]}
      milhar: {n[-4]}\033[m''')
# ----------------------------| Desafio [023]
