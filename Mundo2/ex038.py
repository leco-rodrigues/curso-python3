# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    # O primeiro valor é maior
    # O segundo valor é maior
    # Não existe valor maior, os dois são iguais

# Passo 1: Receber valores para dois "números"
n1 = int(input('Digite o valor do primeiro número: ')) # primeiro número
n2 = int(input('Digite o valor do segundo número: ')) # segundo número

# Passo 2: Criar uma condição aninhada para descobrir e exibir qual o maior ou se são iguais
if n1 > n2:
    print(f'O primeiro número ({n1}) é MAIOR que o segundo número ({n2})!')
elif n1 < n2:
    print(f'O segundo número ({n2}) é MAIOR que o primeiro ({n1})!')
else:
    print(f'Não existe número maior, os dois ({n1} e {n2}) são IGUAIS!')
# ---------------------------------------------------------------------| Desafio [038]
