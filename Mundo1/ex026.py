# Faça um programa que leia uma frase pelo teclado e mostre:
    # Quantas vezes aparece a letra "A".
    # Em que posição ela aparece a primeira vez
    # Em que posição ela aparece a última vez.

# Passo 1: Receber um valor para "frase"
frase = input('\033[7;40mDigite uma frase:\033[m ').strip().upper() # frase convertida em maiúsculo para facilitar

# Passo 2: Descobrir e exibir quantas vezes aparece a letra "A"
print(f'\033[1;34mNa frase "{frase}" a letra "A" aparece {frase.count('A')} vez(es).\033[m') # contagem de aparições

# Passo 3: Criar uma condição simples para descobrir e exibir em que posição ela aparece primeiro e por último
if 'A' in frase.upper():
    print(f'\033[1;34mA letra "A" aparece primeiro na posição {frase.find('A') + 1}.\n' # primeira aparição
          f'E por último na posição {frase.upper().rfind('A') + 1}.\033[m') # última aparição
# ------------------------------------------------------------------------| Desafio [026]
