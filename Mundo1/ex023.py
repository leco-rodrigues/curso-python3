# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
    # Ex: Digite um número: 1834
    #     unidade: 4
    #     dezena: 3
    #     centena: 8
    #     milhar: 1

# Passo 1: Receber um valor para "número"
n = input('\033[7;40mDigite um número de 0 a 9999:\033[m ').strip().replace(' ', '').zfill(4)

# Passo 2: Exibir cada um dos dígitos em unidade, dezena, centena e milhar
print(
      '\033[1;34mClassificando cada um dos dígitos:\n'
      f'unidade: {n[-1]}\n'
      f'dezena: {n[-2]}\n'
      f'centena: {n[-3]}\n'
      f'milhar: {n[-4]}\033[m'
      )
# ----------------------------| Desafio [023]
