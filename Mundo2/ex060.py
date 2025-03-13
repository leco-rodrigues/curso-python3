# Faça um programa que leia um número qualquer e mostre o seu fatorial.
    # Ex:
    # 5! = 5 x 4 x 3 x 2 x 1 = 120

from modulo import txt_style as styl, sep


# Passo 1: Solicitar um valor para "número"
print(styl(sep(6), color_ = 'c'), end = " ")
print(styl("FACTORIAL", 'bd', 'p'), end = " ")
print(styl(sep(6), color_ = 'c'))

num: int = int(input(styl("Enter a number:", 'n') + " "))

# Passo 2: Exibir o fatorial
numbers: list[int] = list(range(num, 0, -1))

print(styl(f"{num}! = " + " x ".join(map(str, numbers)), 'bd', 'p' ))
print(styl(sep(num * 3 + 3), color_ = 'c'))

if num == 1 or num == 0:
    print(styl(str(1), 'bd', 'b'), end = " → ")

fac: int = num
cont: int = 1
while cont < num - 1:
    fac *= (num - cont)
    print(styl(f"{fac}", 'bd', 'b'), end = " → ")
    cont += 1

print(styl("END!", 'bd', 'y'))
# ---------------------------| Desafio [060]
