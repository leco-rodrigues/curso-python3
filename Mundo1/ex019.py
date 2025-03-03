# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice


cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m'}

# Passo 1: Receber valores para quatro "alunos"
aluno1 = input(f"{cores['pretoebranco']}Qual o nome do(a) primeiro(a) aluno(a)?{cores['limpa']} ")
aluno2 = input(f"{cores['pretoebranco']}Qual o nome do(a) segundo(a) aluno(a)?{cores['limpa']} ")
aluno3 = input(f"{cores['pretoebranco']}Qual o nome do(a) terceiro(a) aluno(a)?{cores['limpa']} ")
aluno4 = input(f"{cores['pretoebranco']}Qual o nome do(a) quarto(a) aluno(a)?{cores['limpa']} ")

# Passo 2: Exibir o resultado do sorteio
alunos = [aluno1, aluno2, aluno3, aluno4]
print(f"{cores['negritoroxo']}O(a) aluno(a) sorteado(a) para apagar o quadro foi o(a) {choice(alunos)}!{cores['limpa']}")
# ----------------------------------------------------------------------------------------------------------------------| Desafio [019]
