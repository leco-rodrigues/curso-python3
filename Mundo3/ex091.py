# Jogo de dados em Python:
    # Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
    # Guarde esses resultados em um dicionário.
    # No final, coloque esse dicionário em ordem. sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep


# Passo 1: Solicitar valores aleatórios para 4 "jogadores"
print("----------\nLET'S ROLL THE DICE\n----------\n")

results: dict[str, int] = {}

for j in range(4):
    results[f"Player {j + 1}"] = randint(1, 6)

for k, v in results.items():
    print(f"{k} = {v}")
    sleep(1)

# Passo 2: Exibir o ranking
print("\n----------\nRANKING\n----------\n")

sorted_results = sorted(results.items(), key = lambda x: x[1], reverse = True)

rank: int = 1
for rank, (k, v) in enumerate(sorted_results, start = 1):
    print(f"{rank}º - {k} = {v}")
    rank += 1
    sleep(1)

# Passo 3: Exibir mensagem de encerramento
print("\n----------\nProgram finished. Thanks for playing! 😄\n----------\n")
# ---------------------------------------------------------------------------| AULA 19 - DICIONÁRIOS | DESAFIO [091]
