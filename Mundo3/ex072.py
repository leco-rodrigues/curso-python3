# Números por Extenso:
    # Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20.
    # Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# Extra: Perguntar se o usuário quer executar o programa novamente.

# Passo 1: Criar uma tupla com números de 0 a 20 (escritos por extenso)
number_words: tuple[str, ...] = (
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
    "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
)

# Passo 2: Solicitar um valor entre 0 e 20 para "número"
while True:
    while True:
        try:
            num: int = int(input("Enter a number from 0 to 20: "))

            if 0 <= num <= 20:
                break

            print("Invalid input. Please enter an integer from 0 to 20.")

        except ValueError:
            print("Invalid input. Please enter a valid integer between 0 and 20.")

# Passo 3: Exibir por extenso
    print(f"{num}, written out in full is {number_words[num]}.")

# Passo 4: Solicitar reinício do programa
    while True:
        restart: str = str(input("Do you want to enter another number (y/n)?")).lower()

        if restart in ("yes", "y", "no", "n"):
            break

        print("Invalid input! Please enter 'yes'/'y' or 'no'/'n'.")

    if restart in ("yes", "y"):
        continue
    else:
        break

# Passo 4: Exibir mensagem de encerramento
print("Exiting program... Thank you for using it! 😄")
# ----------------------------------------------------| AULA 16 - TUPLAS | DESAFIO [072]
