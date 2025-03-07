# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}

# Passo 1: Receber três valores para três "retas"
r1 = float(input(f"{cores['pretoebranco']}Digite o comprimento do primeiro lado:{cores['limpa']} "))
r2 = float(input(f"{cores['pretoebranco']}Digite o comprimento do segundo lado:{cores['limpa']} "))
r3 = float(input(f"{cores['pretoebranco']}Digite o comprimento do terceiro lado:{cores['limpa']} "))

# Passo 2: Exibir se é possível formar um triângulo
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f"{cores['negritoazul']}Com {r1}, {r2} e {r3}, é possível formar um triângulo.{cores['limpa']}")
else:
    print(f"{cores['negritoazul']}Com {r1}, {r2} e {r3}, NÃO é possível formar um triângulo.{cores['limpa']}")
# --------------------------------------------------------------------------------------------------------| Desafio [035]
