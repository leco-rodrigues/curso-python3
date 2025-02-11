# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Passo 1: Receber um valor para "salário"
s = float(input('\033[7;40mQual é o seu salário atual?\033[m R$')) # salário

# Passo 2: Calcular e exibir o novo salário
print(f'\033[1;34mR${s:.2f}? O seu novo salário será de R${s * 1.15:.2f}! Um aumento de 15%!\033[m') # novo salário = salário * 1.15
# -------------------------------------------------------------------------------------------------| Desafio [013]
