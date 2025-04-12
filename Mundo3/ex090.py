# Dicionário em Python:
    # Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
    # No final, mostre o conteúdo da estrutura na tela.

def error_message(message: str = "-------\nInvalid input!") -> None:
    print(message)

# Passo 1: Solicitar valores para "nome" e "média"
student_record: dict[str, object] = {}

while True:
    name: str = str(input("-------\nName: ")).strip()
    if (not name) or (not all(c.isalpha() or c.isspace() for c in name)):
        error_message()
        continue
    break

while True:
    try:
        average: float = float(input("-------\nAverage: "))
        if 0 > average or 10 < average:
            error_message()
            continue
        break
    except ValueError:
        error_message()

student_record["Name"] = name
student_record["Average"] = average
student_record["Status"] = "Approved ✅" if average >= 7 else "Failed ❌"

# Passo 2: Exibir conteúdo
print("\n----------\n")
for k, v in student_record.items():
    print(f"{k} = {v}")

# Passo 3: Exibir mensagem de encerramento
print("\n----------\nProgram finished. Thanks for using it! 😄\n----------")
# --------------------------------------------------------------------------| AULA 19 - DICIONÁRIOS | DESAFIO [090]
