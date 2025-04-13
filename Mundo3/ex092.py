# Cadastro de Trabalhador em Python:
    # Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
    # Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (35 anos de colaboração).

from datetime import datetime


# Passo 1: Solicitar valores para "nome", "nascimento" e "CTPS" (com "contratação" e "salário")
print("----------\nSTAFF REGISTRY\n----------\n")

worker_data: dict[str, object] = {}

name: str = "Alex"
birth_year: int = 1999
ctps: int = 2019

# Passo 2: Acrescentar "idade" e "ano de aposentadoria"
current_year = datetime.now().year
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
