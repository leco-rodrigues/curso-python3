# Cálculo do Fatorial:
    # Faça um programa que leia um número qualquer e mostre o seu fatorial.
        # Ex:
        # 5! = 5 x 4 x 3 x 2 x 1 = 120
    # Extra: Usar o "for" loop

from custom_module import txt_style as styl, error_message as err_msg, sepa_rator as sep_


# Passo 1: Solicitar um valor para "número"
print(styl(f"\t{' FACTORIAL ':=^40}", 'bd') + "\n")

while True:
    try:
        num: int = int(input(styl("Please enter a number:", 'n') + " "))
        print(sep_(color = 'c'))
        break

    except ValueError:
        print(sep_(color = 'c'))
        print(err_msg())
        print(sep_(color = 'c'))

# Passo 2: Exibir o fatorial
numbers: list[int] = list(range(num, 0, -1))

print(styl(
    f"{num}! = " + " x ".join(map(str, numbers)) + (" = " if num > 1 else "") + "...", 'bd', 'p' )
      if num != 0 else styl(f"{num}! = 1", 'bd', 'p'
))
print(sep_(color = 'c'))

fac: int = 1
for n in range(num, 1, -1):
    fac *= n
    print(styl(f"{fac}", 'bd', 'b'), end = " → ")

print(styl("END", 'bd', 'g'))

print(sep_(color = 'c'))
print(styl("Exiting program...", 'bd'))
# ------------------------------------| AULA 14 - ESTRUTURA DE REPETIÇÃO "WHILE" | DESAFIO [060-1]
