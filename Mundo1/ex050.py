# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# Passo 1: Receber valores para seis "números"
print('\033[1;35mEscolha seis números inteiros para realizar a soma daqueles que forem pares:\033[m\n')

soma = 0
for num in range(1, 7):
    n = int(input(f'\033[7;40mDigite o {num}° valor:\033[m '))
    if n % 2 == 0:
        soma += n

# Passo 2: Exibir a soma
print(f'\033[1;34mA soma dos números pares dentre os escolhidos é igual a {soma}.\033[m')
# --------------------------------------------------------------------------------------| Desafio [050]
