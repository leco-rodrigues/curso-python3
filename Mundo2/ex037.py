# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
    # 1 para binário
    # 2 para octal
    # 3 para hexadecimal

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m'}

# Passo 1: Receber um valor para "número"
n = int(input(f"{cores['pretoebranco']}Digite um número:{cores['limpa']} "))

# Passo 2: Exibir em binário, octal e hexadecimal, de acordo com a escolha do usuário
conversao = int(input(f"{cores['pretoebranco']}Escolha a base conversão para o número {n} - binário(1), octal(2) ou hexadecimal(3):{cores['limpa']} "))
if conversao == 1:
    print(f"{cores['negritoroxo']}O número {n}, convertido em binário, fica: {bin(n)}.{cores['limpa']}")
elif conversao == 2:
    print(f"{cores['negritoroxo']}O número {n}, convertido em octal, fica: {oct(n)}.{cores['limpa']}")
else:
    print(f"{cores['negritoroxo']}O número {n}, convertido em hexadecimal, fica: {hex(n)}.{cores['limpa']}")
# ---------------------------------------------------------------------------------------------------------| Desafio [037]
