# Cadastro de Trabalhador em Python:
    # Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
    # Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (35 anos de colaboração).

from sys import path
path.append("C:/Users/Usuario/Documents/MeusProjetos/curso-python3")
from functions import txt_style as styl, print_error, sepa_rator as sep_
from datetime import datetime


# Passo 1: Solicitar valores para "nome", "nascimento" e "CTPS" (com "contratação" e "salário")
sep_(10, "c")
print(styl("STAFF REGISTRY", "bd"))
sep_(10, "c")

worker_data: dict[str, object] = {}

while True:
    name: str = str(input(styl("Name: ", "n"))).strip()
    if (not name) or (not all(c.isalpha() or c.isspace() for c in name)):
        print_error("Invalid input! Please enter a valid name.")
        continue
    break

current_year = datetime.now().year
while True:
    try:
        birth_year: int = int(input(styl("Year of birth: ", "n")))
        if 1920 > birth_year or current_year <= birth_year:
            print_error(f"Invalid input! Please enter a valid year between 1920 and {current_year}.")
            continue
        break
    except ValueError:
        print_error("Invalid input! Please enter a valid year.")

while True:
    try:
        ctps: int = int(input(styl("CTPS: (0 to none) ", "n")))
    except ValueError:
        print_error("Invalid input! Please enter a valid year.")

# Passo 2: Acrescentar "idade" e "ano de aposentadoria"
age: int = current_year - birth_year

worker_data["Name"] = name
worker_data["Age"] = age
worker_data["CTPS"] = ctps

if ctps != 0:
    salary: float = 1500.00
    retirement: int = ctps + 35
    worker_data["Salary"] = f"R${salary:.2f}"
    worker_data["Retirement"] = retirement

for k, v in worker_data.items():
    print(f"{k} = {v}")

# Passo : Exibir mensagem de encerramento
print("\n----------\nProgram finished. Thank you for using it! 😄\n----------\n")
# -------------------------------------------------------------------------------| AULA 19 - DICIONÁRIOS | DESAFIO [092]
