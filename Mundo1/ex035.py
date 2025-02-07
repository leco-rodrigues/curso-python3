# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Passo 1: Receber três valores para "três retas"
a = float(input('Digite o comprimento do primeiro lado: ')) # reta a
b = float(input('Digite o comprimento do segundo lado: ')) # reta b
c = float(input('Digite o comprimento do terceiro lado: ')) # reta c

# Passo 2: Criar uma condição composta que diga se é possível formar um triângulo verdadeiro ou não
if a + b > c and a + c > b and b + c > a: # condição para um triângulo verdadeiro
    print('É possível formar um triângulo verdadeiro com essas medidas!')
else:
    print('NÃO é possível formar um triângulo verdadeiro com essas medidas!')
# --------------------------------------------------------------------------- Desafio [035]
