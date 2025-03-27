# Valores únicos em uma Lista
    # Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
    # Caso o número já exista lá dentro, ele não será adicionado.
    # No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Passo 1: Solicitar valores para "número" em uma lista
numbers: list[float] = []

while True:
    while True:
        try:
            num: float = float(input(f"Please enter a number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if num not in numbers:
        numbers.append(num)
        print(f"Number {num} was added to the list.")
    else:
        print(f"The number {num} is already in the list.")

    while True:
        question: str = str(input("Do you want to continue (y/n)? ")).strip().lower()

        if question in ("yes", "y", "no", "n"):
            break
        else:
            print("Invalid input! Please enter 'yes'/'y' or 'no'/'n'.")

    if question in ("yes", "y"):
        continue
    break

print(f"The list is: {', '.join(map(str, numbers))}.")

# Passo 2: Exibir em ordem crescente
print(f"The list in ascending order: {', '.join(map(str, sorted(numbers)))}")

# Passo 3: Exibir mensagem de encerramento
print("Exiting program... Thank you for using it! 😄")
# ----------------------------------------------------| AULA 17 - LISTAS (PARTE 1) | DESAFIO [079]
