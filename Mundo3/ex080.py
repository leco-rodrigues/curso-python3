# Lista ordenada sem repetições
    # Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
    # No final, mostre a lista ordenada na tela.

def ordinal(n: int) -> str:
    return f"{n}{'st' if n == 1 else 'nd' if n == 2 else 'rd' if n == 3 else 'th'}"


# Passo 1: Solicitar cinco valores para "número" em uma lista
numbers: list[float] = []

for n in range(1, 6):
    while True:
        try:
            num: float = float(input(f"Please enter the {ordinal(n)} number: "))
            
            is_inserted = False            
            for i in range(len(numbers)):
                if num <= numbers[i]:
                    numbers.insert(i, num)
                    is_inserted = True
                    print(f"{num} was inserted at position {i} of the list.")
                    break
            
            if not is_inserted:
                numbers.append(num)
                print(f"{num} was inserted at the end of the list.")
            break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Passo 2: Exibir a lista ordenada
print(f"The list in ascending order: {', '.join(map(str, numbers))}.")

# Passo 3: Exibir mensagem de encerramento
print("Exiting program... Thank you for using it! 😄")
# ----------------------------------------------------| AULA 17 - LISTAS (PARTE 1) | DESAFIO [080]
