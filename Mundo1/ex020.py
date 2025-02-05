from random import shuffle


# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e a ordem sorteada.

# Passo 1: Receber quatro valores para "quatro alunos"
aluno1 = input('Qual o nome do(a) primeiro(a) aluno(a)? ')
aluno2 = input('Qual o nome do(a) segundo(a) aluno(a)? ')
aluno3 = input('Qual o nome do(a) terceiro(a) aluno(a) ')
aluno4 = input('Qual o nome do(a) quarto(a) aluno(a)? ')

# Passo 2: Criar uma lista e sortear um ordem
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print(f'A ordem sorteada de apresentação de trabalhos foi {(alunos)}.')
# --------------------------------------------------------------------- Desafio [20]
