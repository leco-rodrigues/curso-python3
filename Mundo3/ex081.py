# Extraindo dados de uma Lista
    # Crie um programa que vai ler vários números e colocar em uma lista.
    # Depois disso, mostre:
        # A) Quantos números foram digitados
        # B) A lista de valores ordenada de dorma decrescente.
        # C) Se o valor 5 foi digitado e está ou não na lista.

# Passo 1: Solicitar valores para "número" em uma lista
numbers: list[float] = []

while True:
    while True:
        try:
            num: float = float(input("Please enter a number: "))
            numbers.append(num)
            break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    while True:
        question: str = str(input("Do you want to continue (y/n)? ")).strip().lower()

        if question in ("yes", "y", "no", "n"):
            break
        print("Invalid input! Please enter 'yes'/'y' or 'no'/'n'.")

    if question in ("no", "n"):
        break

print(f"The list is: {', '.join(map(str, numbers))}")

# Passo 2: Exibir contagem de números
count_num: int = len(numbers)
print(f"There {'are' if count_num > 1 else 'is'} {count_num} element{'s' if count_num > 1 else ''} in this list.")

# Passo 3: Exibir em ordem decrescente
reverse_list: list [float] = sorted(numbers, reverse = True)
print(f"The list in descending order: {', '.join(map(str, reverse_list))}")

# Passo 4: Exibir quantas vezes aparece "5"
count_5: int = numbers.count(5)
if count_5:
    print(f"The number 5 appears {count_5} time{'s' if count_5 > 1 else ''}.")
else:
    print(f"The number 5 does not appear in this list.")

# Passo 5: Exibir mensagem de encerramento
print("Exiting program... Thank you for using it! 😄")
# ----------------------------------------------------| AULA 17 - LISTAS (PARTE 1) | DESAFIO [081]
