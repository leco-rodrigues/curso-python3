# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag).

from Mundo2.custom_module import txt_style as styl, sep


# Passo 1: Solicitar valores para "número inteiro"
print(styl(f"{' SHOW & SUM ':=^40}", 'bd', 'p') + "\n")

numbers: list[int] = []
while True:
    n: int = int(input(styl("Enter a number (999 to stop):", 'n') + " "))

    if n == 999:
        break

    numbers.append(n)

print(styl(sep(15), color_ = 'c'))

# Passo 2: Exibir os números
print(styl(f"You entered {len(numbers):,} numbers.", 'bd', 'b'))
print(styl(sep(15), color_ = 'c'))

# Passo 3: Exibir a soma
sum_ = sum(numbers)
print(styl(f"Their sum is {sum_:,}.", 'bd', 'b'))
print(styl(sep(15), color_ = 'c'))

print(styl("END", 'bd', 'y'))
# --------------------------| AULA 14 - ESTRUTURA DE REPETIÇÃO "WHILE" | DESAFIO [064]
