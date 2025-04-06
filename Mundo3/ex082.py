# Dividindo valores em várias listas:
    # Crie um programa que vai ler vários números e colocar em uma lista.
    # Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
    # Ao final, mostre o conteúdo das três listas geradas.

# Passo 1: Solicitar valores para "números" em uma lista
numbers: list[int] = []
numbers_even: list[int] = []
numbers_odd: list[int] = []

while True:
    try:
        num: int = int(input("Please enter a number: "))
        numbers.append(num)

    except ValueError:
        print(f"Invalid input! Please enter a valid integer.")
        continue

    while True:
        question: str = str(input("Do you want to continue? (y/n) ")).strip().lower()

        if question in ("yes", "y", "no", "n"):
            break
        print("Invalid input! Please enter 'yes'/'y' or 'no'/'n'.")

    if question in ("no", "n"):
        break

for n in numbers:
    if n % 2 == 0:
        numbers_even.append(n)
    else:
        numbers_odd.append(n)

# Passo 2: Exibir a lista
print(f"The list is: {', '.join(map(str, numbers))}")

# Passo 3: Exibir a lista de números pares
print(f"The list of evens is: {', '.join(map(str, numbers_even))}")

# Passo 4: Exibir a lista de números ímpares
print(f"The list of odds is: {', '.join(map(str, numbers_odd))}")

# Passo 5: Exibir mensagem de encerramento
print("Exiting program... Thank you for using it! 😄")
# ----------------------------------------------------| AULA 17 - LISTAS (PARTE 1) | DESAFIO [082]
