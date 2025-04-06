# Mais sobre Matriz em Python:
    # Aprimore o desafio anterior, mostrando no final:
        # A) A soma de todos os valores pares digitados.
        # B) A soma dos valores da terceira coluna.
        # C) O maior valor da segunda linha.

# Passo 1: Solicitar valores para uma "matriz" (3x3)
matriz: list[int] = [
    [],
    [],
    []
]

for n in range(1,10):
    while True:
        try:
            num: int = int(input(f"Please enter the {n}{'st' if n == 1 else 'nd' if n == 2 else 'rd' if n == 3 else 'th'} number for the matrix 3x3: "))

            if len(matriz[0]) < 3:
                matriz[0].append(num)
            elif len(matriz[1]) < 3:
                matriz[1].append(num)
            else:
                matriz[2].append(num)

            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# Passo 2: Exibir a matriz
print(f"{matriz[0]}".replace(",", ""))
print(f"{matriz[1]}".replace(",", ""))
print(f"{matriz[2]}".replace(",", ""))

# Passo 3: Exibir soma dos pares
sum_even: int = 0
for row in matriz:
    for elem in row:
        if elem % 2 == 0:
            sum_even += elem

print(f"The sum of the even numbers of that matriz is {sum_even}.")

# Passo 4: Exibir soma da terceira coluna
sum_3column: int = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f"The sum of the elements in the 3rd column is {sum_3column}.")

# Passo 5: Exibir o maior valor da segunda linha
biggest_2row: int = 0
for elem in matriz[1]:
    if elem > biggest_2row:
        biggest_2row = elem

print(f"The biggest value in the second row is {biggest_2row}.")

# Passo 6: Exibir mensagem de encerramento
print("Exiting program... Thank you for using it! 😄")
# ----------------------------------------------------| AULA 18 - LISTAS (PARTE 2) | DESAFIO [087]
