# Listas com pares e ímpares:
    # Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separadaos os valores pares e ímpares.
    # No final, mostre os valores pares e ímpares em ordem crescente.

# Passo 1: Receber valores para sete "números" em uma lista (separados em pares e ímpares)
numbers: list[int] = [[], []]

for n in range(1, 8):
    while True:
        try:
            num: int = int(input(f"Enter the {n}{'st' if n == 1 else 'nd' if n == 2 else 'rd' if n == 3 else 'th'} number: "))
            
            if num % 2 == 0:
                numbers[0].append(num)
            else:
                numbers[1].append(num)
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# Passo 2: Exibir os valores pares ordem crescente
print(f"The even number{'s are' if len(numbers[0]) > 1 else ' is'}: {sorted(numbers[0])}")

# Passo 3: Exibir os valores ímpares em ordem crescente
print(f"The odd number{'s are' if len(numbers[1]) > 1 else ' is'}: {sorted(numbers[1])}")

# Passo 4: Exibir mensagem de encerramento
print("Exiting program... Thank you for using it! 😄")
# ----------------------------------------------------| AULA 18 - LISTAS (PARTE 2) | DESAFIO [085]
