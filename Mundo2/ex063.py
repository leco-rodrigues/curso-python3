# Escreva um programa que leia um número inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
    # Ex:
    # 0 → 1 → 1 → 2 → 3 → 5 → 8

from modulo import txt_style as styl, sep


# Passo 1: Solicitar um valor para "número inteiro"
print(styl(f"{' FIBONACCI ':=^40}", 'bd', 'p') + "\n")
n: int = int(input(styl("How many elements would you like to see?", 'n') + " "))
print(styl(sep(15), color_ = 'c'))

# Passo 2: Exibir os "n" primeiros elementos de uma Sequência Fibonacci
print(styl("0 → 1 → ", 'bd', 'b'), end = "")

fib0 = 0
fib1 = 1
cont = 0
while cont < n - 2:
    fibn = fib0 + fib1
    print(styl(f"{fibn}", 'bd', 'b'), end = " → ")
    fib0 = fib1
    fib1 = fibn
    cont += 1

print(styl("END", 'bd', 'y'))
# --------------------------| Desafio [063]
