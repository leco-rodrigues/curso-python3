# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date


cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m'}

# Passo 1: Receber um valor para "ano"
ano = int(input(f"{cores['pretoebranco']}Digite um ano qualquer (0 = ano atual):{cores['limpa']} "))

# Passo 2: Exibir se é "bissexto" ou não
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    if ano > 2025:
        print(f"{cores['negritoroxo']}{ano} será um ano bissexto.{cores['limpa']}")
    else:
        print(f"{cores['negritoroxo']}{ano} foi um ano bissexto.{cores['limpa']}")
else:
    if ano > 2025:
        print(f"{cores['negritoroxo']}{ano} NÃO será um ano bissexto.{cores['limpa']}")
    elif ano < 2025:
        print(f"{cores['negritoroxo']}{ano} NÃO foi um ano bissexto.{cores['limpa']}")
    else:
        print(f"{cores['negritoroxo']}{ano} NÃO é um ano bissexto.{cores['limpa']}")
# ---------------------------------------------------------------------------------| Desafio [032]
