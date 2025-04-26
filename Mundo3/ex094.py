# Unindo dicionários e listas:
    # Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
    # No final, mostre:
        # A) Quantas pessoas foram cadastradas.
        # B) A média de idade do grupo.
        # C) Uma lista com todas as mulheres.
        # D) Uma lista com todas as pessoas com idade acima da média.

def yes_or_no(question: str = "Do you want to continue?") -> bool:
    prompt: str = "\n----------\n" + question.strip() + " "
    while True:
        answer: str = str(input(prompt)).strip().lower()
        if answer in ("yes", "y", "no", "n"):
            if answer in ("yes", "y"):
                return True
            return False
        print("Please enter 'yes'/'y' or 'no'/'n'.")


# Passo 1: Solicite valores para "nome", "sexo" e "idade"
registration_list: list[dict[str, object]] = []
sum_age: float = 0
woman_list: list[str] = []
above_average_age: list[str] = []

print("\n-------\nREGISTRATION\n-------\n")

while True:
    registration_dict: dict[str, object] = {}
    while True:
        try:
            name: str = str(input("Name: ")).strip().title()
            if (not name) or (not all(c.isalpha() or c.isspace() for c in name)):
                raise ValueError("That name is invalid. Please check.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    while True:
        try:
            sex: str = str(input("Sex: (M/F) ")).strip().lower()
            if (not sex) or (sex not in ("masculine", "m", "male", "feminine", "f", "female")):
                raise ValueError("Please enter 'masculine'/'m'/'male' or 'feminine'/'f'/'female'.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    while True:
        try:
            age: int = int(input("Age: "))
            if (not age) or (0 > age or age > 122):
                raise ValueError("Please enter a valid age (0-122).")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    registration_dict["Name"] = name
    normalized_sex: str = "female" if sex in ("feminine", "f", "female") else "male"
    registration_dict["Sex"] = normalized_sex
    registration_dict["Age"] = age
    sum_age += age
    registration_list.append(registration_dict.copy())

    if normalized_sex == "female":
        woman_list.append(name)

    if not yes_or_no("Do you want to register another person? (y/n)"):
        break

# Passo 2: Exibir número de pessoas registradas
print("\n----------\nREGISTRATION DATA\n----------\n")

num_registrations: int = len(registration_list)
print(f"-------\nRegistered people: {num_registrations}\n-------")

# Passo 3: Exibir a média de idade
average_age = sum_age / num_registrations if num_registrations > 0 else 0
print(f"Average age: {int(average_age)}\n-------")

# Passo 4: Exibir uma lista com as mulheres
if woman_list:
    print(f"List of women: {', '.join(woman_list)}\n-------")
else:
    print("There are no women registered.\n-------")

# Passo 5: Exibir uma lista com as pessoas acima da média
for person in registration_list:
    if person["Age"] > average_age:
        above_average_age.append(person["Name"])

print(f"List of people above average age: {', '.join(above_average_age)}\n-------")

# Passo 6: Exibir mensagem de encerramento
print("\n----------\nProgram finished. Thanks for using it! 😄\n----------\n")
# ----------------------------------------------------------------------------| AULA 19 - DICIONÁRIOS | DESAFIO [094]
