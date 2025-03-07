# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime


# Passo 1: Receber sete valores para "anos de nascimento"
ano_atual = datetime.today().year
maior_18 = 0
menor_18 = 0

for pessoa in range(1, 8):
    ano_nasc = int(input(f'\033[7;40mAno de nascimento da {pessoa}° pessoa:\033[m '))
    idade = ano_atual - ano_nasc

    if idade >= 18:
        maior_18 += 1
    else:
        menor_18 += 1

# Passo 2: Exibir quantas pessoas são maiores de idade
print(f'\033[1;35m{maior_18} dessas pessoas já são maiores de idade.\033[m')

# Passo 3: Exibir quantas pessoas são menores de idade
print(f'\033[1;35m{menor_18} dessas pessoas ainda são menores de idade.\033[m')
# ----------------------------------------------------------------------------| Desafio [054]
