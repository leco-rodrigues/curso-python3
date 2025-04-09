# Palpites para a Mega Sena:
    # Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
    # O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import sample
from time import sleep


# Passo 1: Solicitar um valor para "jogos"
print("----------\nMEGA SENA NUMBER PICKER\n----------\n")

games_guesses: list[list[int]] = []

while True:
    user_input: str = input("How many games would you like to generate? ")
    if not user_input.isdigit() or int(user_input) <= 0:
        print("-------\nInvalid input! Please enter a positive integer.\n-------")
        continue

    games: int = int(user_input)
    break

# Passo 2: Exibir palpites
print(f"\n----------\nGENERATING {games} GAMES\n----------\n")

print("-------")
for count in range(games):
    games_guesses.append(sorted(sample(range(1, 61), 6)))

    print(f"Game {count + 1}: {games_guesses[count]}")
    print("-------")
    sleep(1)

# Passo 3: Exibir mensagem de encerramento
print("Program finished. Thank you for using it! 😄")
# ---------------------------------------------------| AULA 18 - LISTAS (PARTE 2) | DESAFIO [088]
