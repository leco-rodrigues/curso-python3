# Faça um programa que leia um número qualquer e mostre o seu fatorial.
    # Ex:
    # 5! = 5 x 4 x 3 x 2 x 1 = 120

from modulo import txt_style as styl, sep


# Passo 1: Solicitar um valor para "número"
num: int = int(input(styl("Escolha um número:", 'n') + " "))
cont: int = 1
fac: int = num * (num - cont)

# Passo 2: Exibir o fatorial
numbers: list[str] = []
for n in range(num, 0, -1):
    numbers.append(n)

print(styl(f"{num}! = " + " x ".join(map(str, numbers)), 'bd', 'p' ))
print(styl(f"{sep(num * 3)}", color_ = 'c'))

while cont < num - 1:
    print(styl(f"{fac}", 'bd', 'b'), end = " → ")
    cont += 1
    fac = fac * (num - cont)

print(styl("FIM!", 'bd', 'y'))
# ---------------------------| Desafio [060]
