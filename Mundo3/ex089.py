# Boletim com listas compostas:
    # Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
    # No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


def yes_no(question: str = "Do you want to continue? (y/n) ") -> bool:
    while True:
        choice: str = str(input(question))
        if choice not in ("yes", "y", "no", "n"):
            error_message("-------\nInvalid input! Please enter 'yes'/'y' or 'no'/'n'.")
            continue
        if choice in ("yes", "y"):
            return True
        return False

def error_message(message: str = "Invalid input!") -> None:
    print(message)

# Passo 1: Solicitar valores para "nome" e "notas" em uma lista composta
student_grades: list[list[object]] = []

while True:
    while True:
        name: str = str(input("-------\nName: ")).strip()
        if (not name) or (not all(c.isalpha() or c.isspace() for c in name)):
            error_message("-------\nInvalid input! Please enter a valid name.")
            continue
        break

    while True:
        try:
            grade1: float = float(input("-------\nGrade 1: "))
            if 0 > grade1 or 10 < grade1:
                error_message("-------\nInvalid input! Please enter a grade between 0 and 10.")
                continue
            break
        except ValueError:
            error_message("-------\nInvalid input! Please enter a valid grade.")

    while True:
        try:
            grade2: float = float(input("-------\nGrade 2: "))
            if 0 > grade2 or 10 < grade2:
                error_message("-------\nInvalid input! Please enter a grade between 0 and 10.")
                continue
            break
        except ValueError:
            error_message("-------\nInvalid input! Please enter a valid grade.")

    average: float = (grade1 + grade2) / 2
    data_temp: list[list[object]] = [name, [grade1, grade2], average]
    student_grades.append(data_temp)

    if not yes_no("----------\n\nDo you want to add another student's grade? (y/n) "):
        break

# Passo 2: Exibir a média
print(f"\n ----------\n{'Nº':<3} | {'NAME':<13}| {'AVERAGE'}\n" + "-" * 28)
for i in range(len(student_grades)):
    print(f"{i:03} | {student_grades[i][0]:<13}| {student_grades[i][2]:<.1f}")

print(" ----------\n")

# Passo 3: Exibir notas individualmente
while True:
    if not yes_no("-------\nDo you want to see a student's grades? (y/n) "):
        break

    while True:
        try:
            student: int = int(input("-------\nEnter the student's number: "))
            if student >= len(student_grades):
                error_message(f"-------\nInvalid input! Please enter a valid number (0 to {len(student_grades) - 1}).")
                continue
            break
        except ValueError:
            error_message("-------\nInvalid input! Please enter a valid number.")
            continue

    grades: list[float] = student_grades[student][1]
    print(f"-------\nName: {student_grades[student][0]} | Grades: {grades[0]:.1f}, {grades[1]:.1f}")

# Passo 4: Exibir mensagem de encerramento
print("\n----------\nProgram finished. Thanks for using it! 😄\n----------\n")
# ----------------------------------------------------------------------------| AULA 18 - LISTAS (PARTE 2) | DESAFIO [089]
