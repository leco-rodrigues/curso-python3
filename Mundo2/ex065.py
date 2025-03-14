# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

from Mundo2.custom_module import txt_style as styl, sep


# Passo 1: Solicitar valores para "número inteiro"
print(styl(f"{' MEAN ':=^40}", 'bd', 'p') + "\n")

numbers: list[int] = []
while True:
    num: int = int(input(styl("Enter a number:", 'n') + " "))
    numbers.append(num)

    add_num: str = str(input(styl("Would you like to enter one more number (s/n)?", 'n') + " "))
    if add_num == 'n':
        break

print(styl(sep(15), color_ = 'c'))

# Passo 2: Exibir a média
mean = sum(numbers) / len(numbers)
print(styl(f"The mean between these numbers is {mean:,.2f}.", 'bd', 'b'))
print(styl(sep(15), color_ = 'c'))

# Passo 3: Exibir o maior
print(styl(f"The biggest number is {max(numbers)}.", 'bd', 'b'))
print(styl(sep(15), color_ = 'c'))

# Passo 4: Exibir o menor
print(styl(f"The lowest number is {min(numbers)}.", 'bd', 'b'))
print(styl(sep(15), color_ = 'c'))

print(styl("END", 'bd', 'y'))
# --------------------------| AULA 14 - ESTRUTURA DE REPETIÇÃO "WHILE" | DESAFIO [065]
