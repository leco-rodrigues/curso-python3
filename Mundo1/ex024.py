# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# Passo 1: Receber um valor para "cidade"
cidade = input('Digite o nome de uma cidade: ')

# Passo 2: Descobrir se começa com "SANTO"
if 'SANTO' in cidade.upper().strip().split()[0]: # nome da cidade convertido em maiúsculo
    print('O nome dessa cidade começa com "SANTO"!')
else:
    print('O nome dessa cidade NÃO começa com "SANTO"!')
# ------------------------------------------------------ Desafio [024]
