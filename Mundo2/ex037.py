# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
    # 1 para binário
    # 2 para octal
    # 3 para hexadecimal

# Passo 1: Receber um valor para "número"
n = int(input('Digite um número inteiro: ')) # número inteiro

# Passo 2: Criar um condição aninhada para converter e exibir em binário, octal e hexadecimal
conversao = int(input(f'Para qual base de conversão deseja converter o número {n}, binário(1), octal(2) ou hexadecimal(3)? '))
if conversao == 1:
    print(f'O número {n}, convertido em binário, fica: {bin(n)}.') # conversão para binário
elif conversao == 2:
    print(f'O número {n}, convertido em octal, fica: {oct(n)}.') # conversão para octal
else:
    print(f'O número {n}, convertido em hexadecimal, fica: {hex(n)}.') # conversão para hexadecimal
# -------------------------------------------------------------------| Desafio [037]
