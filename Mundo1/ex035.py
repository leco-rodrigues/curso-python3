# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}

# Passo 1: Receber três valores para três "retas"
a = float(input(f"{cores['pretoebranco']}Digite o comprimento do primeiro lado:{cores['limpa']} "))
b = float(input(f"{cores['pretoebranco']}Digite o comprimento do segundo lado:{cores['limpa']} "))
c = float(input(f"{cores['pretoebranco']}Digite o comprimento do terceiro lado:{cores['limpa']} "))

# Passo 2: Exibir se é possível formar um triângulo
if a + b > c and a + c > b and b + c > a:
    print(f"{cores['negritoazul']}Com {a}, {b} e {c}, é possível formar um triângulo.{cores['limpa']}")
else:
    print(f"{cores['negritoazul']}Com {a}, {b} e {c}, NÃO é possível formar um triângulo.{cores['limpa']}")
# --------------------------------------------------------------------------------------------------------| Desafio [035]
