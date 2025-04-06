# Matriz em Python:
    # Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
    # No final, mostre a matriz na tela, com a formatação correta.

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

# Passo 3: Exibir mensagem de encerramento
print("Exiting program... Thank you for using it! 😄")
# ----------------------------------------------------| AULA 18 - LISTAS (PARTE 2) | DESAFIO [086]
