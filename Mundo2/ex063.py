# Sequência de Fibonacci v1.0:
    # Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
        # Ex:
        # 0 → 1 → 1 → 2 → 3 → 5 → 8

from custom_module import txt_style as styl, print_error, sepa_rator as sep_


# Passo 1: Solicitar um valor para "número inteiro"
print(styl(f"\t{' FIBONACCI ':=^40}", 'bd') + "\n")

while True:
    try:
        num: int = int(input(styl("How many elements would you like to see?", 'n') + " "))
        break
    except ValueError:
        print_error(16)

print(sep_(16, 'c'))

# Passo 2: Exibir os "n" primeiros elementos de uma Sequência Fibonacci
print(styl("0 → 1 → ", 'bd', 'b'), end = "")

term_1 = 0
term_2 = 1
cont = 1
while cont <= num - 2:
    current_term = term_1 + term_2
    print(styl(f"{current_term}", 'bd', 'b'), end = " → ")
    term_1 = term_2
    term_2 = current_term
    cont += 1

print(styl("END", 'bd', 'y'))

print(sep_(16, 'c'))
print(styl("Exiting program...", 'bd'))
# ------------------------------------| AULA 14 - ESTRUTURA DE REPETIÇÃO "WHILE" | DESAFIO [063]
