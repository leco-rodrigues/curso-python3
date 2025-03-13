# Cálculo do Fatorial:
    # Faça um programa que leia um número qualquer e mostre o seu fatorial.
        # Ex:
        # 5! = 5 x 4 x 3 x 2 x 1 = 120

from custom_module import txt_style as styl, error_message as err_msg, sepa_rator as sep_


# Passo 1: Solicitar um valor para "número"
print(styl(f"\t{' FACTORIAL ':=^40}", 'bd') + "\n")

while True:

    try:
        num: int = int(input(styl("Enter a number:", 'n') + " "))
        print(sep_(color = 'c'))
        break

    except ValueError:
        print(sep_(color = 'c'))
        print(err_msg())
        print(sep_(color = 'c'))

# Passo 2: Exibir o fatorial
numbers: list[int] = list(range(num, 0, -1))

print(styl(f"{num}! = " + " x ".join(map(str, numbers)), 'bd', 'p' ))
print(sep_(color = 'c'))

if num == 1 or num == 0:
    print(styl(str(1), 'bd', 'p'), end = " → ")

fac: int = num
cont: int = 1
while cont < num - 1:
    fac *= (num - cont)
    print(styl(f"{fac}", 'bd', 'b'), end = " → ")
    cont += 1

print(styl("END", 'bd', 'g'))

print(sep_(color = 'c'))
print(styl("Terminating program...", 'bd'))
# ----------------------------------------| AULA 14 - ESTRUTURA DE REPETIÇÃO "WHILE" | DESAFIO [060]
