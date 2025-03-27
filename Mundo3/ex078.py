# Maior e Menor valores na Lista
    # Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
    # No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# Passo 1: Solicitar 5 valores para "números" em uma lista
numbers: list[float] = []

for n in range(5):
    while True:
        try:
            num: float = float(input(f"Please enter a number for position {n}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

print(f"The list is: {', '.join(map(str, numbers))}")

# Passo 2: Exibir o maior número e sua posição
print(f"The largest number is {max(numbers)} and it's in position(s)", end = " ")

numMax: int = 0
for n in numbers:
    if n == max(numbers):
        print(f"{numbers.index(n, numMax)}...", end = " ")
        numMax = numbers.index(n, numMax) + 1

# Passo 3: Exibir o menor número e sua posição
print(f"\nThe smallest number is {min(numbers)} and it's in position(s)", end = " ")

numMin: int = 0
for n in numbers:
    if n == min(numbers):
        print(f"{numbers.index(n, numMin)}...", end = " ")
        numMin = numbers.index(n, numMin) + 1

# Passo 4: Exibir mensagem de encerramento
print("\nExiting program... Thank you for using it! 😄")
# ------------------------------------------------------| AULA 17 - LISTAS (PARTE 1) | DESAFIO [078]
