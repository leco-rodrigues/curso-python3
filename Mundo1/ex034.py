# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

# Passo 1: Receber um valor para "salário"
salario = float(input('\033[7;40mDigite o seu salário atual: R$'))

# Passo 2: Exibir novo salário
if salario > 1250:
    print(f'\033[1;34mR${salario:.2f}? Você receberá um aumento de 10%, seu novo salário será de R${salario * 1.10:.2f}!\033[m')
else:
    print(f'\033[1;34mR${salario:.2f}? Você receberá um aumento de 15%, seu novo salário será de R${salario * 1.15:.2f}!\033[m')
# -----------------------------------------------------------------------------------------------------------------------------| Desafio [034]
