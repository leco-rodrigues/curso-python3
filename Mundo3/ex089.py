# Boletim com listas compostas:
    # Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
    # No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

# Passo 1: Solicitar valores para "nome" e "notas" em uma lista composta
print("----------\n SCHOOL GRADES\n----------\n")

grades: list[list[str, int]] = [[], []]

while True:
    name: str = str(input("-------\nStudent's name: ")).strip()
    if (not name and all(c.isalpha() or c.isspace() for c in name)):
        print("-------\nInvalid input! Please enter a valid name.")
        continue
    grades[0].append(name)

    i: int = 1
    while i <= 2:
        try:
            grade: float = float(input(f"Grade {i}: "))
        except ValueError:
            print("-------\nInvalid input! Please enter a valid grade.\n-------\n")
            continue
        grades[1].append(grade)
        i += 1

    while True:
        question: str = str(input("\n-------\nDo you want to enter more school grades? (y/n) "))
        if question in ("yes", "y", "no", "n"):
            break
        print("-------\nInvalid input! Please enter 'yes'/'y' or 'no'/'n'.")

    if question in ("no", "n"):
        break

# Passo 2: Exibir a média de cada um
print("-------")
print("\n----------\n MEDIA \n----------\n")

i: int = 0
while i < len(grades[0]):
    for grade in range(0, len(grades[1]), 2):
        media: float = (grades[1][grade] + grades[1][grade + 1]) / 2
        print(f"-------\nThe student {grades[0][i]}'s media is {media}.\n-------\n")
        i += 1

# Passo 3: Exibir individualmente
while True:
    try:
        student: int = int(input(f"-------\nWhat student's grades do you want to see? (0 to {len(grades[0]) - 1}) "))
        if 0 > student or student >= len(grades[0]):
            print(f"-------\nInvalid input! Please enter a valid index (0 to {len(grades[0]) - 1}).")
            continue
    except ValueError:
        print(f"-------\nInvalid input! Please enter a valid index (0 to {len(grades[0]) - 1}).")
        continue

    if student == 0:
        media = (grades[1][student] + grades[1][student + 1]) / 2
        print(f"-------\nThe student {grades[0][student]}'s media is {media}.\n-------\n")
    else:
        media = (grades[1][student + 1] + grades[1][student + 2]) / 2
        print(f"-------\nThe student {grades[0][student]}'s media is {media}.\n-------\n")

    while True:
        question: str = str(input("-------\nDo you want to see another student's grade? (y/n) "))
        if question in ("yes", "y", "no", "n"):
            break
        print("-------\nInvalid input! Please enter 'yes'/'y' or 'no'/'n'.")

    if question in ("no", "n"):
        break

print("-------\n")

# Passo 4: Exibir mensagem de encerramento
print("Program finished. Thanks for using it! 😄")
# ------------------------------------------------| AULA 18 - LISTAS (PARTE 2) | DESAFIO [089]
