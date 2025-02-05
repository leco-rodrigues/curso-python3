from random import shuffle


# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e a ordem sorteada.

# Passo 1: Receber quatro valores de "aluno" e formar uma lista com esses valores
aluno1 = input('Qual o nome do(a) primeiro(a) aluno(a)? ')
aluno2 = input('Qual o nome do(a) segundo(a) aluno(a)? ')
aluno3 = input('Qual o nome do(a) terceiro(a) aluno(a) ')
aluno4 = input('Qual o nome do(a) quarto(a) aluno(a)? ')
alunos = [aluno1, aluno2, aluno3, aluno4]

# Passo 2: Exibir o nome de cada aluno dessa lista numa ordem aleatória
shuffle(alunos)
print(f'A ordem sorteada de apresentação de trabalhos foi {(alunos)}.')
# --------------------------------------------------------------------- Desafio [20]
