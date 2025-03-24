# Maior e menor valores em Tupla:
    # Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
    # Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint


# Passo 1: Criar uma tupla com cinco "números" aleatórios
numbers: tuple[int, ...] = (randint(0, 100),randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

# Passo 2: Exibir a listagem
print(f"Os números nessa tupla são: {numbers}")

# Passo 3: Exibir o menor
print(f"\nO menor número é: {min(numbers)}")

# Passo 4: Exibir o maior
print(f"\nO maior número é: {max(numbers)}")

# Passo 5: Exibir mensagem de encerramento
print("\nExiting program... Thank you for using it! 😄")
# ------------------------------------------------------| AULA 16 - TUPLAS | DESAFIO [074]
