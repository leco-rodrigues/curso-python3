# Faça um programa que leia uma frase pelo teclado e mostre:
    # Quantas vezes aparece a letra "A".
    # Em que posição ela aparece a primeira vez
    # Em que posição ela aparece a última vez.

# Passo 1: Receber um valor para "frase"
frase = input('\033[7;40mDigite uma frase:\033[m ').strip()

# Passo 2: Exibir quantas vezes a letra "A" aparece
if 'A' in frase.upper():
    print(
          f'\033[1;34mNa frase "{frase}", a letra "A" aparece {frase.upper().count("A")} vez(es).\n'

# Passo 3: Exibir em que posição a letra "A" aparece primeiro
          f'A letra "A" aparece primeiro na posição {frase.upper().find("A") + 1}.\n'

# Passo 4: Exibir em que posição a letra "A" aparece por último
          f'A letra "A" aparece por último na posição {frase.upper().rfind("A") + 1}.\033[m'
          )
else:
    print(f'\033[1;35mA letra "A" NÃO aparece na frase "{frase}".\033[m')
# ----------------------------------------------------------------------| Desafio [026]
