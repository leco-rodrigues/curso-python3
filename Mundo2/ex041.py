# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    # Até 9 anos: MIRIM
    # Até 14 anos: INFANTIL
    # Até 19 anos: JUNIOR
    # Até 20 anos: SÊNIOR
    # Acima: MASTER

# Passo 1: Receber um valor para "ano de nascimento"
ano_nascimento = int(input('Digite o ano do seu nascimento: '))

# Passo 2: Criar uma condição aninhada que exiba a categoria do atleta, de acordo com a idade
idade = 2025 - ano_nascimento
if idade <= 9: # categoria mirim
    print(f'Esse atleta tem {idade} anos, o que o coloca na categoria MIRIM.')
elif 9 < idade <=14: # categoria infantil
    print(f'Esse atleta tem {idade} anos, o que o coloca na categoria INFANTIL.')
elif 14 < idade <= 19: # categoria júnior
    print(f'Esse atleta tem {idade} anos, o que o coloca na categoria JUNIOR.')
elif idade == 20: # categoria sênior
    print(f'Esse atleta tem {idade} anos, o que o coloca na categoria SÊNIOR.')
else: # categoria master
    print(f'Esse atleta tem {idade} anos, o que o coloca na categoria MASTER.')
# ----------------------------------------------------------------------------| Desafio [041]
