# Tratando de vários valores v1.0:
    # Crie um programa que leia vários números inteiros pelo teclado.
    # O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
    # No final, mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag).

from custom_module import txt_style as styl, print_error, sepa_rator as sep_


# Passo 1: Solicitar valores para "número inteiro"
print(styl(f"\t{' SHOW & SUM ':=^40}", 'bd') + "\n")

numbers: list[int] = []
while True:
    try:
        n: int = int(input(styl("Please enter a number (999 to stop):", 'n') + " "))

        if n == 999:
            break

        numbers.append(n)

    except ValueError:
        print_error()

print(sep_(15, 'c'))

# Passo 2: Exibir os números
print(styl(f"You entered {len(numbers):,} {'numbers' if len(numbers) > 1 else 'number'}.", 'bd', 'p'))
print(sep_(15, 'c'))

# Passo 3: Exibir a soma
sum_ = sum(numbers)
if len(numbers) > 1:
    print(styl(f"Their sum is {sum_:,}.", 'bd', 'p'))
else:
    print(styl(f"The number is {numbers[0]}.", 'bd', 'p'))

print(sep_(15, 'c'))
print(styl("Exiting program...", 'bd'))
# ------------------------------------| AULA 14 - ESTRUTURA DE REPETIÇÃO "WHILE" | DESAFIO [064]
