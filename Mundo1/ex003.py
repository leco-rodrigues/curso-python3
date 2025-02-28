# Crie um programa que leia dois números e mostre a soma entre eles.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}

# Passo 1: Receber valores para dois "números"
n1 = float(input(f"{cores['pretoebranco']}Digite o valor do primeiro número:{cores['limpa']} ")) # primeiro número
n2 = float(input(f"{cores['pretoebranco']}Digite o valor do segundo número:{cores['limpa']} ")) # segundo número

# Passo 2: Calcular e exibir a soma
print(f"{cores['negritoazul']}{n1} + {n2} = {n1 + n2}.{cores['limpa']}")
# ---------------------------------------------------------------------| Desafio [003]
