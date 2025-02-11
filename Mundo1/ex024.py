# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# Passo 1: Receber um valor para "cidade"
cidade = input('\033[7;40mDigite o nome de uma cidade:\033[m ')

# Passo 2: Criar uma condição composta para descobrir e exibir se começa com "SANTO" ou não
if 'Santo' in cidade.title().strip().split()[0]: # primeiro nome da cidade convertido em "title" para comparação
    print('\033[1;35mO nome dessa cidade começa com "Santo"!\033[m')
else:
    print('\033[1;35mO nome dessa cidade NÃO começa com "Santo"!\033[m')
# ---------------------------------------------------------------------| Desafio [024]
