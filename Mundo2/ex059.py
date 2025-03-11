# Crie um programa que leia dois valores e mostre um menu na tela:
    # [1] somar
    # [2] multiplicar
    # [3] maior
    # [4] novos números
    # [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from modulo import txt_style as styl, sep


# Passo 1: Receber valores para dois "números"
numbers: list[int] = []

print(styl(f"\nNumbers: {numbers[0]}, {numbers[1]}", 'bd', 'p'))

print(styl("\nChoose an opition:", 'bd', 'p'))
print(styl(
    """
    [ 1 ] Add
    [ 2 ] Multiply
    [ 3 ] Find the biggest number
    [ 4 ] Enter new numbers
    [ 5 ] Exit program
    """,
    'bd', 'p'
))

choice:int | None = None
while choice not in range(1, 6):
    choice = int(input(styl("Choice:", 'n') + " "))
    print(styl(sep(15), color_ = 'c'))

    if choice == 1:
        print(styl(f"The sum of those numbers is equal to {sum(numbers)}.", 'bd', 'b'))

    elif choice == 2:
        print(styl(f"The product of those numbers is equal to {numbers[0] * numbers[1]}.", 'bd', 'b'))

    elif choice == 3:
        print(styl(f"The biggest number between those is {max(numbers)}.", 'bd', 'b'))

    elif choice == 4:
        print()

    elif choice == 5:
        print(styl("Adeus!", 'db', 'p'))
        break

    break

print(styl(sep(15), color_ = 'c'))
print(styl("Encerrando o programa.", 'bd', 'r'))
# ---------------------------------------------| Desafio [059]
