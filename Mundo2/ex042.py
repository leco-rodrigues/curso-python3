# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    # Equilátero: todos os lados iguais
    # Isósceles: dois lados iguais
    # Escaleno: todos os lados diferentes

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m', 'negritoroxo':'\033[1;35m'}

# Passo 1: Receber valores para três "retas"
r1 = float(input(f"{cores['pretoebranco']}Digite o comprimento do primeiro lado:{cores['limpa']} "))
r2 = float(input(f"{cores['pretoebranco']}Digite o comprimento do segundo lado:{cores['limpa']} "))
r3 = float(input(f"{cores['pretoebranco']}Digite o comprimento do terceiro lado:{cores['limpa']} "))

# Passo 2: Exibir se é possível formar um triângulo
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f"{cores['negritoazul']}Com {r1}, {r2} e {r3}, é possível formar um triângulo.{cores['limpa']}")

# Passo 3: Exibir o tipo de triângulo
    if r1 == r2 == r3:
        print(f"{cores['negritoroxo']}{r1}, {r2} e {r3} formam um triângulo equilátero, ou seja, todos os lados são iguais.{cores['limpa']}")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print(f"{cores['negritoroxo']}{r1}, {r2} e {r3} formam um triângulo isósceles, ou seja, dois lados são iguais.{cores['limpa']}")
    else:
        print(f"{cores['negritoroxo']}{r1}, {r2} e {r3} formam um triângulo escaleno, ou seja, todos os lados são diferentes.{cores['limpa']}")

else:
    print(f"{cores['negritoazul']}Com {r1}, {r2} e {r3}, NÃO é possível formar um triângulo.{cores['limpa']}")
# --------------------------------------------------------------------------------------------------------| Desafio [042]
