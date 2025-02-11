# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e a ordem sorteada.


from random import shuffle


cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m'}
# Passo 1: Receber valores para quatro "alunos"
aluno1 = input(f'{cores["pretoebranco"]}Qual o nome do(a) primeiro(a) aluno(a)?{cores['limpa']} ')
aluno2 = input(f'{cores["pretoebranco"]}Qual o nome do(a) segundo(a) aluno(a)?{cores['limpa']} ')
aluno3 = input(f'{cores["pretoebranco"]}Qual o nome do(a) terceiro(a) aluno(a){cores['limpa']} ')
aluno4 = input(f'{cores["pretoebranco"]}Qual o nome do(a) quarto(a) aluno(a)?{cores['limpa']} ')

# Passo 2: Criar uma lista e exibi-la em uma ordem aleatória
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print(f'{cores['negritoroxo']}A ordem sorteada de apresentação de trabalhos foi {(alunos)}.{cores["limpa"]}')
# ----------------------------------------------------------------------------------------------------------| Desafio [20]
