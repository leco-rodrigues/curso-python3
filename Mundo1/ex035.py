# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m'}
# Passo 1: Receber três valores para três "retas"
a = float(input(f'{cores['pretoebranco']}Digite o comprimento do primeiro lado:{cores['limpa']} ')) # reta a
b = float(input(f'{cores['pretoebranco']}Digite o comprimento do segundo lado:{cores['limpa']} ')) # reta b
c = float(input(f'{cores['pretoebranco']}Digite o comprimento do terceiro lado:{cores['limpa']} ')) # reta c

# Passo 2: Criar uma condição composta que diga se é possível formar um triângulo ou não
if a + b > c and a + c > b and b + c > a: # condição para um triângulo verdadeiro
    print(f'{cores['negritoroxo']}É possível formar um triângulo verdadeiro com essas medidas!({a}, {b} e {c}){cores['limpa']}')
else:
    print(f'{cores['negritoroxo']}NÃO é possível formar um triângulo verdadeiro com essas medidas! ({a}, {b} e {c}){cores['limpa']}')
# ----------------------------------------------------------------------------------------------------------------------------------| Desafio [035]
