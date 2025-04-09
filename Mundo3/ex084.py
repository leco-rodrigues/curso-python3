# Lista composta e análise de dados:
    # Faça um programa que leia nome e peso de vários pessoas, guardando tudo em uma lista.
    # No final, mostre:
        # A) Quantas pessoas foram cadastradas.
        # B) Uma listagem com as pessoas mais pesadas
        # C) Uma listagem com as pessoas mais leves.

# Passo 1: Solicitar valores para "nome" e "peso" em uma lista
people: list[str, float] = []
data: list[str, float] = []
count_people: int = 0
heaviest_person: list[str] = []
lightest_person: list[str] = []
heaviest_weight: float = 0
lightest_weight: float = 0

while True:
    while True:
        name: str = str(input("Name: ")).strip()
        if not name and not (name.isalpha() or name.isspace()):
            print("Invalid input! Please enter a valid name.")
            continue
        data.append(name)
        break

    while True:
        try:
            weight: float = float(input("Weight: "))
            data.append(weight)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    people.append(data[:])
    count_people += 1
    data.clear()

    if (heaviest_weight and lightest_weight) == 0:
        heaviest_weight = weight
        lightest_weight = weight
        heaviest_person.append(name)
        lightest_person.append(name)

    elif weight > heaviest_weight:
        heaviest_weight = weight
        heaviest_person.clear()
        heaviest_person.append(name)

    elif weight == heaviest_weight:
        heaviest_person.append(name)

    elif weight < lightest_weight:
        lightest_weight = weight
        lightest_person.clear()
        lightest_person.append(name)

    elif weight == lightest_weight:
        lightest_person.append(name)

    while True:
        question: str = str(input("Do you want to continue? (y/n) "))
        if question in ("yes", "y", "no", "n"):
            break
        print("Invalid input! Please enter 'yes'/'y' or 'no'/'n'.")

    if question in ("no", "n"):
        break

# Passo 2: Exibir quantos foram cadastrados
print(f"Numbers of registered people: {count_people}")

# Passo 3: Exibir lista dos mais pesados
print(f"The heaviest weight is {heaviest_weight} kg and the person{'s are' if len(heaviest_person) > 1 else ' is'}: {heaviest_person}")

# Passo 4: Exibir lista dos mais leves
print(f"The lightest weight is {lightest_weight} kg and the person{'s are' if len(lightest_person) > 1 else ' is'}: {lightest_person}")

# Passo 5: Exibir mensagem de encerramento
print("Program finished. Than you for using it! 😄")
# --------------------------------------------------| AULA 18 - LISTAS (PARTES 2) | DESAFIO [084]
