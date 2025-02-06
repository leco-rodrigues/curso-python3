# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

# Passo 1: Receber um valor para "nome"
nome = input('Nome: ')

# Passo 2: Descobrir se tem "SILVA"
if 'SILVA' in nome.upper(): # nome convertido em maiúsculo
    print('Tem "SILVA" no nome!')
else:
    print('NÃO tem "SILVA" no nome!')
# ----------------------------------- Desafio [026]
