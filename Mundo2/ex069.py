# Análise de dados do grupo:
    # Crie um programa que leia a idade e o sexo de várias pessoas.
    # A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
    # No final, mostre:
        # A) Quantas pessoas tem mais de 18 anos.
        # B) Quantos homens foram cadastrados.
        # C) Quantas mulheres tem menos de 20 anos.

from custom_module import txt_style as styl, print_error, sepa_rator as sep_


# Passo 1: Solicitar valores para "idade" e "sexo"
print(styl(f"\t{' REGISTRATION ':=^40}\n", 'bd'))

older_than_18: int = 0
count_man: int = 0
woman_younger_20: int = 0

while True:

    while True:
        try:
            age: int = int(input(styl("Age:", 'n') + " "))

            if 0 < age < 120:

                if age > 18:
                    older_than_18 += 1

                break

            else:
                print_error("Invalid input. Please enter an age between 0 and 120.")

        except ValueError:
            print_error("Invalid input. Please enter an integer.")

    while True:
        gender: str = str(input(styl("Gender (M/F)", 'n') + " ")).strip().lower()

        if gender in ("m", "f"):

            if gender == 'm':
                count_man += 1

            break

        else:
            print_error("Invalid input. Please enter 'M' for masculine or 'F' for feminine.")

    if age < 20 and gender == 'f':
        woman_younger_20 += 1

    while True:
        choice = str(input(styl("Do you want to register one more person (Y/N)?", 'n') + " ")).strip().lower()

        if choice in ("yes", "y", "no", "n"):
            break
        else:
            print_error("Invalid input. Please enter 'yes'/'y' or 'no'/'n'.")

    if choice in ('no', 'n'):
        break

sep_(color = 'c')

# Passo 2: Exibir quantos tem mais de 18 anos
print(styl(f"Number of registered persons older than 18 years: {older_than_18}", 'bd', 'p'))
sep_(color = 'c')

# Passo 3: Exibir quantos são homens
print(styl(f"Number of registered men: {count_man}", 'bd', 'p'))
sep_(color = 'c')

# Passo 4: Exibir quantos são mulheres com menos de 20 anos
print(styl(f"Number of registered woman younger than 20 years: {woman_younger_20}", 'bd', 'p'))
sep_(color = 'c')

# Passo 5: Exibir mensagem de encerramento
print(styl("Exiting the program... Thank you for using it! 😄"))
# --------------------------------------------------------------| AULA 15 - INTERROMPENDO REPETIÇÕES "WHILE" | DESAFIO [069]
