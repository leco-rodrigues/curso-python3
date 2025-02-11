# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu,


from random import randint
from time import sleep


cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m', 'ciano':'\033[6m'}
# Passo 1: Sortear um número inteiro entre 0 e 5 e receber um valor para "número"
n_sorteado = randint(0, 5) # número inteiro aleatório entre 0 a 5
n_escolhido = int(input(f'{cores['pretoebranco']}Qual você acha que foi o número sorteado entre 0 e 5?{cores['limpa']} ')) # número escolhido
print(f'{cores['ciano']}--=--{cores['limpa']}' * 7)
print(f'{cores['negritoroxo']}Deixa eu alterar o número aqui...{cores['limpa']}') # falsa pegadinha
print(f'{cores['ciano']}--=--{cores['limpa']}' * 7)
sleep(3)

# Passo 2: Criar uma condição composta e exibir se acertou ou não
if n_escolhido == n_sorteado: # condição de acerto
    print(f'{cores['negritoroxo']}HAHA! Brincadeira!{cores['limpa']}')
    sleep(1)
    print(f'{cores['negritoroxo']}Você acertou! PARABÉNS!{cores['limpa']}')
    print(f'{cores['ciano']}--=--{cores['limpa']}' * 7)
else:
    print(f'{cores['negritoroxo']}HAHA! Brincadeira!{cores['limpa']}')
    sleep(1)
    print(f'{cores['negritoroxo']}Mas você errou... O número era {n_sorteado}.{cores['limpa']}')
    print(f'{cores['ciano']}--=--{cores['limpa']}' * 7)
# ----------------------------------------------------| Desafio [029]
