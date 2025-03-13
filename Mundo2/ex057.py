# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

from modulo import txt_style as styl, sep


# Passo 1: Solicitar um valor para "sexo"
print(styl(sep(3), color_ = 'c'), end = " ")
print(styl("SIGN UP INFORMATION", 'bd', 'p'), end = " ")
print(styl(sep(3), color_ = 'c') + "\n")

name: str = str(input(styl("Name:", 'n') + " ")).strip().upper()
age: int = int(input(styl("Age:", 'n') + " "))

while True:
    sex: str = str(input(styl('Gender (M/F):', 'n') + " ")).strip().upper()
    if sex in ('M', 'F'):
        break
    print(styl('Please enter "M" for male or "F" for female.', 'bd', 'r'))
# -----------------------------------------------------------------------| Desafio [054]
