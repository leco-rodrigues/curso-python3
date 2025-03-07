# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    # Até 9 anos: MIRIM
    # Até 14 anos: INFANTIL
    # Até 19 anos: JUNIOR
    # Até 25 anos: SÊNIOR
    # Acima: MASTER

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}

# Passo 1: Receber um valor para "ano de nascimento"
ano_nascimento = int(input(f"{cores['pretoebranco']}Digite o ano do seu nascimento:{cores['limpa']} "))

# Passo 2: Exibir a categoria, de acordo com a idade
idade = 2025 - ano_nascimento
if idade <= 9:
    print(f"{cores['negritoazul']}Esse atleta tem {idade} anos, o que o coloca na categoria MIRIM.{cores['limpa']}")
elif idade <=14:
    print(f"{cores['negritoazul']}Esse atleta tem {idade} anos, o que o coloca na categoria INFANTIL.{cores['limpa']}")
elif idade <= 19:
    print(f"{cores['negritoazul']}Esse atleta tem {idade} anos, o que o coloca na categoria JUNIOR.{cores['limpa']}")
elif idade <= 25:
    print(f"{cores['negritoazul']}Esse atleta tem {idade} anos, o que o coloca na categoria SÊNIOR.{cores['limpa']}")
else:
    print(f"{cores['negritoazul']}Esse atleta tem {idade} anos, o que o coloca na categoria MASTER.{cores['limpa']}")
# ------------------------------------------------------------------------------------------------------------------| Desafio [041]
