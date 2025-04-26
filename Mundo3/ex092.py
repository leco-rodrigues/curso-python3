# Cadastro de Trabalhador em Python:
    # Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
    # Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (35 anos de colaboração).

from sys import path
path.append("C:/Users/Usuario/Documents/MeusProjetos/Passa-Tempo/Misc")
from functions import txt_style as styl, print_error, sepa_rator as sep_, name_it
from datetime import datetime

def year_birth(question: str = "Year of birth:") -> int:
    prompt: str = question.strip()
    while True:
        try:
            birth_year: int = int(input(styl(prompt, "n") + " "))
            if 1920 > birth_year or current_year <= birth_year:
                print_error(f"Invalid input! Please enter a valid year between 1920 and {current_year}.")
                continue
            return birth_year
        except ValueError:
            print_error("Invalid input! Please enter a valid year.")

# Passo 1: Solicitar valores para "nome", "ano de nascimento" e "CTPS" e calcular "idade"
sep_(10, "c")
print(styl("STAFF REGISTRY", "bd"))
sep_(10, "c")

worker_data: dict[str, object] = {}

name = name_it()
current_year = datetime.now().year
birth_year = year_birth()
age: int = current_year - birth_year

while True:
    try:
        ctps: int = int(input(styl("CTPS: (0 to none)", "n") + " "))
        break
    except ValueError:
        print_error("Invalid input! Please enter a valid CTPS.")

worker_data["Name"] = name
worker_data["Age"] = age
worker_data["CTPS"] = ctps

# Passo 2: Calcular "ano de aposentadoria" e solicitar um valor para "salário"
if ctps != 0:
    while True:
        try:
            hire_year: int = int(input(styl("Year of hire:", "n") + " "))
            if (hire_year < birth_year + 18) or (hire_year > current_year):
                print_error("Invalid input! Year of hire must be after 18 years old and not in the future.")
                continue
            break
        except ValueError:
            print_error("Invalid input! Please enter a valid year.")
    while True:
        try:
            salary: float = float(input(styl("Salary:", "n") + " R$"))
            break
        except ValueError:
            print_error("Invalid input! Please enter a valid salary.")

    retirement_year: int = hire_year + 35
    retirement_age: int = (hire_year - birth_year) + 35
    worker_data["Year of hire"] = hire_year
    worker_data["Salary"] = f"R${salary:.2f}"
    worker_data["Retirement"] = str(retirement_year) + f", ({retirement_age} years)"

# Passo 3: Exibir informações
sep_(10, "c")
print("WORKER'S INFO")
sep_(10, "c")

for k, v in worker_data.items():
    print(f"{k} = {v}")

# Passo 4: Exibir mensagem de encerramento
sep_(10, "c")
print(styl("Program finished. Thank you for using it! 😄", "bd"))
sep_(10, "c")
# ---------------------------------------------------------------| AULA 19 - DICIONÁRIOS | DESAFIO [092]
