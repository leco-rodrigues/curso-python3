# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

# Passo 1: Receber um valor para "salário"
sm = float(input('Digite o seu salário atual: R$')) # salário

# Passo 2: Criar que uma condição que calcule o aumento dependendo do salário
if sm > 1250: # condição de aumento de 10% (sm * 1.10)
    print(f'R${sm:.2f}? Você receberá um aumento de 10%, seu novo salário será de R${sm * 1.10:.2f}.')
else:
    print(f'R${sm:.2f}? Você receberá um aumento de 15%, seu novo salário será de R${sm * 1.15:.2f}.') # aumento de 15% (sm * 1.15)
# ---------------------------------------------------------------------------------------------------- Desafio [034]
