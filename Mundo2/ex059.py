# Crie um programa que leia dois valores e mostre um menu na tela:
    # [1] somar
    # [2] multiplicar
    # [3] maior
    # [4] novos números
    # [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from custom_module import txt_style as styl, entry_validation as ent_val, sepa_rator as sep_
from time import sleep


# Passo 1: Solicitar valores para dois "números"
title: str = " CHOOSE THE NUMBERS "
options: str = """[ 1 ] Add
[ 2 ] Multiply
[ 3 ] Find the biggest number
[ 4 ] Enter new numbers
[ 5 ] Exit program"""

numbers: list[int] = []
while True:

    if not numbers:
        print(styl(f"\t{title:=^40}\n", 'bd'))

        for n in range(1, 3):
            num: int = int(input(styl(f"{n}° número:", 'n') + " "))
            numbers.append(num)

    num1, num2 = numbers

    sleep(1)

    print(sep_(color = 'c'))
    print(styl(f"Numbers: {", ".join(map(str, numbers))}", 'bd', 'p'))
    print(styl("\nOptions:", 'bd'))
    print(styl(f"{options}", 'bd'))

    print(sep_(color = 'c'))
    choice = int(input(styl("Choose an option:", 'n') + " "))
    print(sep_(color = 'c'))

# Passo 2: Exibir a soma
    if choice == 1:
        print(styl(
            f"The sum between {num1} + {num2}" +
            f" is equal to {sum(numbers):,}.", 'bd', 'b'
        ))

# Passo 3: Exibir o produto
    elif choice == 2:
        print(styl(
            f"The product between {num1} x {num2}" +
            f" is equal to {num1 * num2:,}.", 'bd', 'b'
        ))

# Passo 4: Exibir o maior número
    elif choice == 3:
        print(styl(
            f"The biggest number between {num1} and {num2}" +
            f" is {max(numbers):,}.", 'bd', 'b'))

# Passo 5: Solicitar novos valores
    elif choice == 4:
        numbers.clear()

# Passo 6: Encerrar o programa
    elif choice == 5:
        print(styl("END", 'bd'))
        break

    # Exibe mensagem de erro para entradas inválidas
    else:
        print(ent_val())
# ---------------------| AULA 14 - ESTRUTURA DE REPETIÇÃO "WHILE" | DESAFIO [059]
