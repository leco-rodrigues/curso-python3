# Análise de dados em uma Tupla:
    # Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
    # No final mostre:
        # A) Quantas vezes apareceu o valor 9.
        # B) Em que posição foi digitado o primeiro valor 3.
        # C) Quais foram os números pares.

# Passo 1: Solicitar quatro valores para "número"
numbers: tuple[int, ...] = tuple(int(input(f"Please enter the {i}º number: ")) for i in range(1, 5))
print(f"The numbers entered are: {', '.join(map(str, numbers))}")

# Passo 2: Exibir quantas vezes apareceu o 9
if numbers.count(9) > 0:
    print(f"\nNumber 9 appeared {numbers.count(9)} time(s).")
else:
    print(f"\nNumber 9 does not appear.")

# Passo 3: Exibir em que posição apareceu o primeiro 3
if 3 in numbers:
    print(f"\nNumber 3 first appeared in position {numbers.index(3) + 1}.")
else:
    print("\nNumber 3 does not appear.")

# Passo 4: Exibir os pares
even_numbers: list[int] = [num for num in numbers if num % 2 == 0]

if even_numbers:
    print(f"\nThe even number{'s are' if len(even_numbers) > 1 else ' is'} {', '.join(map(str, even_numbers))}.")
else:
    print("\nThere are no even numbers.")

# Passo 5: Exibir mensagem de encerramento
print("\nExiting program... Thank you for using it! 😄")
# ------------------------------------------------------| AULA 16 - TUPLAS | DESAFIO [075]
