# Cadastro de Jogador de Futebol:
    # Crie um programa que gerencie o performance de um jogador de futebol.
    # O programa vai ler o nome do jogador e quantas partidas ele jogou.
    # Depois vai ler a quantidade de gols feitos em cada partida.
    # No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

def yes_or_no(question: str = "Do you want to continue? (y/s)") -> bool:
    prompt: str = question.strip() + " "
    while True:
        answer: str = str(input(prompt)).lower()
        if answer in ("yes", "y", "no", "n"):
            if answer in ("yes", "y"):
                return True
            return False
        print("----------\nPlease enter 'yes'/'y' or 'no'/'n'.")

def get_integer(question: str = "Enter the number:") -> int:
    prompt: str = question.strip() + " "
    while True:
        try:
            number: int = int(input(prompt))
            return number
        except ValueError as e:
            print(f"Invalid input: {e}")


# Passo 1: Solicitar valores para "jogador", "partidas"
performance_record: dict[int, dict[str, object]] = {}
performance: dict[str, object] = {}
id: int = 0

while True:
    while True:
        try:
            name: str = str(input("Name: ")).strip().title()
            if (not name) or (not all(c.isalpha() or c.isspace() for c in name)):
                raise ValueError("Empty space or non-letter characters are not accepted.")
            performance["Player"] = name
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    while True:
        try:
            matches: int = int(input("Number of matches: "))
            if matches >= 0:
                if matches <= 0:
                    print(f"The player {name} did not play any matches.")
                break
        except ValueError as e:
            print(f"Invalid input: {e}")

# Passo 2: Solicitar valor para "gols" e calcular o "total"
    goals: list[int] = []
    if matches > 0:
        for i in range(matches):
            while True:
                try:
                    goal: int = int(input(f"Numbers of goals in match {i + 1}: "))
                    if goal or goal == 0:
                        break
                except ValueError as e:
                    print(f"Invalid input: {e}")
            goals.append(goal)
    else:
        goals = [0]

    total: int = sum(goals)
    performance["Goals"] = goals
    performance["Total"] = total

# Passo 3: Exibir o "performance"
    print(f"\n----------\nThe player {performance["Player"]} played in {matches} match{'es' if matches != 1 else ""}.\n----------")
    for i, g in enumerate(performance["Goals"]):
        print(f"-> Match {i + 1}: {g} goal{'s' if g != 1 else ''}")
    print("----------")
    print(f"Total goals: {performance["Total"]}\n----------\n")
    
    performance_record[id] = performance.copy()
    
    while True:
        if yes_or_no("\n----------\nDo you want see the records? (y/n)"):
            while True:
                choice: int = get_integer("Enter the ID:")
                if choice in range(len(performance_record)):
                    print(performance_record[choice])
                    break
                print("That ID is not register on the list. Please check.")
            continue
        break

    print("----------")

    if not yes_or_no("Do you want to register another player? (y/n)"):
        break

    id += 1

# Passo 4: Exibir mensagem de encerramento
print("\n----------\nProgram finished. Thanks for using it! 😄\n----------\n")
# ----------------------------------------------------------------------------| AULA 19 - DICIONÁRIOS | DESAFIO [093]
