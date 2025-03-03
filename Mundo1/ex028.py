# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep


cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m', 'ciano':'\033[36m'}

# Passo 1: Receber um valor aleatório entre 0 e 5 para "número"
n_sorteado = randint(0, 5)
n_palpite = int(input(f"{cores['pretoebranco']}Qual você acha que foi o número sorteado entre 0 e 5?{cores['limpa']} "))

print(f"{cores['ciano']}--=--{cores['limpa']}" * 7)
print(f"{cores['negritoroxo']}Deixa eu alterar o número aqui...{cores['limpa']}") # Pegadinha
print(f"{cores['ciano']}--=--{cores['limpa']}" * 7)

sleep(1)

print(f"{cores['negritoroxo']}Haha! Brincadiera!")
print(f"{cores['ciano']}--=--{cores['limpa']}" * 7)

sleep(1)

# Passo 2: Exibir o resultado
if n_palpite == n_sorteado:
    print(f"{cores['negritoroxo']}Você acertou! PARABÉNS!{cores['limpa']}")
    print(f"{cores['ciano']}--=--{cores['limpa']}" * 7)
else:
    print(f"{cores['negritoroxo']}Mas você errou... O número era {n_sorteado}.{cores['limpa']}")
    print(f"{cores['ciano']}--=--{cores['limpa']}" * 7)
# ----------------------------------------------------| Desafio [028]
