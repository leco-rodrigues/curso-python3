# Crie um programa que leia um frase qualquer e diga se ele é um palíndrmo, desconsiderando espaços.
# Ex:
    # APOS A SOPA
    # A SACADA DA CASA
    # A TORRE DA DERROTA
    # O LOBO AMA O BOLO
    # ANOTARAM A DATA DA MARATONA

# Passo 1: Receber um valor para "frase"
frase = input('\033[7;40mDigite uma frase qualquer:\033[m\n').strip().upper()

# Passo 2: Exibir se é um palíndromo
if frase.replace(' ', '') == frase.replace(' ', '')[::-1]:
    print('\033[1;35mEssa frase é um palíndromo.\033[m')
else:
    print('\033[1;35mEssa frase NÃO é um palíndromo.\033[m')
# ---------------------------------------------------------| Desafio [053]
