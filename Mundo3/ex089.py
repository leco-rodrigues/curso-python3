# Boletim com listas compostas:
    # Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
    # No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

# Passo 1: Solicitar valores para "nome" e duas "notas" em uma lista composta
grades: list[list[str, int]] = [[], []]

while True:
    name: str = str(input("Student's name: "))
    if not name.isalpha():
        print("Invalid input! Please enter a valid name.")
        continue
    grades[0].append(name)

    for i in range(2):
        grade: float = float(input(f"{i + 1}"))

# Passo : Exibir mensagem de encerramento
print("Program finished. Thanks for using it! 😄")
# ------------------------------------------------| AULA 18 - LISTAS (PARTE 2) | DESAFIO [089]
