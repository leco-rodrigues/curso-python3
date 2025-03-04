# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    # Equilátero: todos os lados iguais
    # Isósceles: dois lados iguais
    # Escaleno: todos os lados diferentes

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m', 'negritoroxo':'\033[1;35m'}

# Passo 1: Receber valores para três "retas"
a = float(input(f"{cores['pretoebranco']}Digite o comprimento do primeiro lado:{cores['limpa']} "))
b = float(input(f"{cores['pretoebranco']}Digite o comprimento do segundo lado:{cores['limpa']} "))
c = float(input(f"{cores['pretoebranco']}Digite o comprimento do terceiro lado:{cores['limpa']} "))

# Passo 2: Exibir se é possível formar um triângulo
if a + b > c and a + c > b and b + c > a:
    print(f"{cores['negritoazul']}Com {a}, {b} e {c}, é possível formar um triângulo.{cores['limpa']}")

# Passo 3: Exibir o tipo de triângulo
    if a == b == c:
        print(f"{cores['negritoroxo']}{a}, {b} e {c} formam um triângulo equilátero, ou seja, todos os lados são iguais.{cores['limpa']}")
    elif not a == b == c and a == b or a == c or b == c:
        print(f"{cores['negritoroxo']}{a}, {b} e {c} formam um triângulo isósceles, ou seja, dois lados são iguais.{cores['limpa']}")
    else:
        print(f"{cores['negritoroxo']}{a}, {b} e {c} formam um triângulo escaleno, ou seja, todos os lados são diferentes.{cores['limpa']}")

else:
    print(f"{cores['negritoazul']}Com {a}, {b} e {c}, NÃO é possível formar um triângulo.{cores['limpa']}")
# --------------------------------------------------------------------------------------------------------| Desafio [042]
