# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# Passo 1: Exibir os números pares
print('\033[1;35mOs números pares entre 1 e 50 são:\033[m\n')

for par in range(1, 50):
    if par % 2 == 0:
        print(f'\033[1;34m{par} |\033[m', end=' ')
# -----------------------------------------------| Desafio [047]
