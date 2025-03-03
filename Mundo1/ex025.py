# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

# Passo 1: Receber um valor para "nome"
nome = input('\033[7;40m]Digite o nome de uma pessoa:\033[m ')

# Passo 2: Exibir se tem "SILVA"
if 'Silva' in nome.title(): # Ignora variações de maiúsculas/minúsculas
    print('\033[1;35mTem "Silva" no nome!\033[m')
else:
    print('\033[1;35mNÃO tem "Silva" no nome!\033[m')
# --------------------------------------------------| Desafio [025]
