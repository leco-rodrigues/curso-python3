# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    # O primeiro valor é maior
    # O segundo valor é maior
    # Não existe valor maior, os dois são iguais

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}

# Passo 1: Receber valores para dois "números"
n1 = int(input(f"{cores['pretoebranco']}Digite o valor do primeiro número:{cores['limpa']} "))
n2 = int(input(f"{cores['pretoebranco']}Digite o valor do segundo número:{cores['limpa']} "))

# Passo 2: Exibir qual o maior ou se são iguais
if n1 > n2:
    print(f"{cores['negritoazul']}O primeiro número ({n1}) é MAIOR que o segundo ({n2})!{cores['limpa']}")
elif n1 < n2:
    print(f"{cores['negritoazul']}O segundo número ({n2}) é MAIOR que o primeiro ({n1})!{cores['limpa']}")
else:
    print(f"{cores['negritoazul']}Não existe número maior, ambos ({n1} e {n2}) são IGUAIS!{cores['limpa']}")
# ---------------------------------------------------------------------------------------------------------| Desafio [038]
