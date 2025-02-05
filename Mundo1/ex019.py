from random import choice


# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

# Passo 1: Receber quatro valores de "aluno" e formar uma lista com esse valores
aluno1 = input('Qual o nome do(a) primeiro(a) aluno(a)? ')
aluno2 = input('Qual o nome do(a) segundo(a) aluno(a)? ')
aluno3 = input('Qual o nome do(a) terceiro(a) aluno(a)? ')
aluno4 = input('Qual o nome do(a) quarto(a) aluno(a)? ')
alunos = [aluno1, aluno2, aluno3, aluno4]

# Passo 2: Sortear um desses valores dessa lista
print(f'O(a) aluno(a) sorteado(a) foi {choice(alunos)}!')
# ------------------------------------------------------- Desafio [019]
