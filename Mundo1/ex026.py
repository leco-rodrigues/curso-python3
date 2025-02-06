# Faça um programa que leia uma frase pelo teclado e mostre:
    # Quantas vezes aparece a letra "A".
    # Em que posição ela aparece a primeira vez
    # Em que posição ela aparece a última vez.

# Passo 1: Receber um valor para "frase"
frase = input('Digite uma frase: ').strip().upper()

# Passo 2: Descobrir quantas vezes aparece a letra "A"
print(f'Na frase "{frase}" a letra "A" aparece {frase.count('A')} vez(es).') # contagem de aparições

# Passo 3: Descobrir em que posição ela aparece (ou se não aparece)
if 'A' in frase.upper():
    print(f'A letra "A" aparece primeiro na posição {frase.find('A') + 1}.\n' # primeira aparição
          f'E por último na posição {frase.upper().rfind('A') + 1}.') # última aparição
else:
    print('A letra "A" não aparece nessa frase.') # letra "A" inexistente
# ----------------------------------------------- Desafio [026]
