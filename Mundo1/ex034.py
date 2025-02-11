# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}
# Passo 1: Receber um valor para "salário"
sm = float(input(f'{cores['pretoebranco']}Digite o seu salário atual:{cores['limpa']} R$')) # salário

# Passo 2: Criar uma condição composta que calcule o aumento dependendo do salário
if sm > 1250: # condição de aumento de 10% (sm * 1.10)
    print(f'{cores['negritoazul']}R${sm:.2f}? Você receberá um aumento de 10%, seu novo salário será de R${sm * 1.10:.2f}!{cores['limpa']}')
else:
    print(f'{cores['negritoazul']}R${sm:.2f}? Você receberá um aumento de 15%, seu novo salário será de R${sm * 1.15:.2f}!{cores['limpa']}') # aumento de 15% (sm * 1.15)
# -----------------------------------------------------------------------------------------------------------------------------------------| Desafio [034]
