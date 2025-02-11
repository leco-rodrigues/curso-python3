# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

# Passo 1: Receber um valor para "nome"
nome = input('Nome: ') # nome completo

# Passo 2: Criar uma condição composta para descobrir e exibir se tem "SILVA" ou não
if 'Silva' in nome.title(): # nome convertido em "title" para comparação
    print('Tem "Silva" no nome!')
else:
    print('NÃO tem "Silva" no nome!')
# ----------------------------------| Desafio [026]
