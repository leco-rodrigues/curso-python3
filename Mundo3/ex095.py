# Aprimorando os dicionários:
    # Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

def yes_or_no(question: str = "Do you want to continue? (y/n)") -> bool:
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
            print(f"-------\nInvalid input: {e}\n-------")


# Passo 1: Solicitar valores para "jogador", "partidas"
performance_record: dict[int, dict[str, object]] = {}
player_id: int = 0

while True:
    performance: dict[str, object] = {}
    while True:
        try:
            name: str = str(input("Name: ")).strip().title()
            if (not name) or (not all(c.isalpha() or c.isspace() for c in name)):
                raise ValueError("Empty space or non-letter characters are not accepted.")
            performance["Player"] = name
            break
        except ValueError as e:
            print(f"-------\nInvalid input: {e}\n-------")

    while True:
        try:
            matches: int = int(input("Number of matches: "))
            if matches >= 0:
                if matches <= 0:
                    print(f"The player {name} did not play any matches.")
                break
        except ValueError as e:
            print(f"-------\nInvalid input: {e}\n-------")

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
                    print(f"-------\nInvalid input: {e}\n-------")
            goals.append(goal)
    else:
        goals = [0]

    total: int = sum(goals)
    performance["Goals"] = goals
    performance["Total"] = total

# Passo 3: Exibir a "performance"
    print(f"\n----------\nThe player {performance["Player"]} played in {matches} match{'es' if matches != 1 else ""}.\n----------")
    for i, g in enumerate(performance["Goals"]):
        print(f"-> Match {i + 1}: {g} goal{'s' if g != 1 else ''}")
    print("----------")
    print(f"Total goals: {performance["Total"]}\n----------\n")
    
    performance_record[player_id] = performance.copy()
    
    while True:
        if yes_or_no("\n----------\nDo you want see the records? (y/n)"):
            while True:
                print("\n----------\nREGISTERED PLAYERS\n----------")
                for p_id, p_data in performance_record.items():
                    print(f"ID: {p_id} | {p_data["Player"]}")
                print("\n-------")

                choice: int = get_integer("Enter the ID: (-1 to cancel)")
                if choice in range(len(performance_record)):
                    print(f"-------\n{performance_record[choice]}\n-------\n")
                    break
                if choice == -1:
                    break
                print("-------\nThat ID is not registered on the list. Please check.\n-------")
            if choice == -1:
                break
            continue
        break

    print("----------")

    if not yes_or_no("Do you want to register another player? (y/n)"):
        break

    player_id += 1

# Passo 4: Exibir mensagem de encerramento
print("\n----------\nProgram finished. Thanks for using it! 😄\n----------\n")
# ----------------------------------------------------------------------------| AULA 19 - DICIONÁRIOS | DESAFIO [095]
