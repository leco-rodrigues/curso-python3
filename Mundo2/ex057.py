# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.

from Mundo2.custom_module import txt_style as styl, sep


# Passo 1: Solicitar um valor para "sexo"
print(styl(sep(4), color_ = 'c'), end = " ")
print(styl("SIGN UP INFORMATION", 'bd', 'p'), end = " ")
print(styl(sep(4), color_ = 'c') + "\n")

name: str = str(input(styl("Name:", 'n') + " ")).strip().upper()
age: int = int(input(styl("Age:", 'n') + " "))

while True:
    sex: str = str(input(styl('Gender (M/F):', 'n') + " ")).strip().upper()[0]
    print(styl(sep(15), color_ = 'c'))
    if sex in 'MmFf':
        break
    print(styl('Please enter "M" for male or "F" for female.', 'bd', 'r'))
    print(styl(sep(15), color_ = 'c'))

print(styl("END", 'bd', 'y'))
# --------------------------| Desafio [054]
