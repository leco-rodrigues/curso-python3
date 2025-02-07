# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu,


from random import randint
from time import sleep


# Passo 1: Sortear um número inteiro entre 0 e 5 e receber um valor para "número escolhido"
n_sorteado = randint(0, 5) # número inteiro aleatório entre 0 a 5
n_escolhido = int(input('Qual você acha que foi o número sorteado entre 0 e 5? ')) # número escolhido
print('Deixa eu alterar o número aqui...')
sleep(2)

# Passo 2: Criar uma condição composta que diga que se acertou ou não
if n_escolhido == n_sorteado: # condição de acerto
    print('HAHA! Brincadeira!')
    sleep(1)
    print('Você acertou! PARABÉNS!')
else:
    print('HAHA! Brincadeira!')
    sleep(1)
    print(f'Mas você errou... O número era {n_sorteado}.')
# -------------------------------------------------------- Desafio [029]
