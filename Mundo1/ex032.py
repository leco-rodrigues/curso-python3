# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date


# Passo 1: Receber um valor para "ano"
ano = int(input('Digite um ano qualquer (0 = ano atual): '))

# Passo 2: Criar um função composta que diga se um ano é bissexto ou não
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    if ano > 2025:
        print(f'{ano} será um ano bissexto.')
    else:
        print(f'{ano} foi um ano bissexto.')
else:
    if ano > 2025:
        print(f'{ano} NÃO será um ano bissexto.')
    elif ano < 2025:
        print(f'{ano} NÃO foi um ano bissexto.')
    else:
        print(f'{ano} NÃO é um ano bissexto.')
# -------------------------------------------- Desafio [032]
