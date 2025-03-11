# Crie um programa que leia dois valores e mostre um menu na tela:
    # [1] somar
    # [2] multiplicar
    # [3] maior
    # [4] novos números
    # [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from modulo import txt_style as styl, sep


# Passo 1: Solicitar valores para dois "números"
title: str = "CHOOSE THE NUMBERS:"
options: str = """
[ 1 ] Add
[ 2 ] Multiply
[ 3 ] Find the biggest number
[ 4 ] Enter new numbers
[ 5 ] Exit program
"""
choice: int | None = None
numbers: list[int] = []

while True:

    if not numbers:
        print(styl(sep(4), color_ = 'c'), end = " ")
        print(styl(f"{title}", 'bd', 'p'), end = " ")
        print(styl(sep(4), color_ = 'c'), end = "\n")

        for num in range(1, 3):
            n: int = int(input(styl(f"{num}° número:", 'n') + " "))
            numbers.append(n)

        print(styl(f"\nNumbers: {", ".join(map(str, numbers))}", 'bd', 'p'))
        print(styl("\nChoose one option:", 'bd', 'p'))
        print(styl(options, 'bd', 'p'))

    print(styl(sep(15), color_ = 'c'))
    choice = int(input(styl("Choose an option:", 'n') + " "))
    print(styl(sep(15), color_ = 'c'))

# Passo 2: Exibir a soma
    if choice == 1:
        print(styl(f"The sum of those numbers is equal to {sum(numbers)}.", 'bd', 'b'))

# Passo 3: Exibir o produto
    elif choice == 2:
        print(styl(f"The product of those numbers is equal to {numbers[0] * numbers[1]}.", 'bd', 'b'))

# Passo 4: Exibir o maior número
    elif choice == 3:
        print(styl(f"The biggest number among them is {max(numbers)}.", 'bd', 'b'))

# Passo 5: Solicitar novos valores
    elif choice == 4:
        numbers.clear()

# Passo 6: Encerrar o programa
    elif choice == 5:
        print(styl("Terminating program...", 'bd', 'y'))
        break

    # Exibe mensagem de erro para entradas inválidas
    else:
        print(styl("Please enter a valid option.", 'bd', 'r'))
# -----------------------------------------------------------| Desafio [059]
