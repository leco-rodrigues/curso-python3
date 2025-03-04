# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint


cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m'}

# Passo 1: Receber valores para "jogador1" e "jogador2"
escolhas = {1:'pedra', 2:'papel', 3:'tesoura'}
jogador = input(f"{cores['pretoebranco']}Jogador, escolha 'pedra', 'papel' ou 'tesoura':{cores['limpa']} ")
computador = f'{escolhas[randint(1, 3)]}'

# Passo 2: Exibir o resultado
if jogador == 'pedra':
    
    if computador == 'tesoura':
        print(f"{cores['negritoroxo']}Jogador VENCEU!{cores['limpa']}")
    elif computador == 'papel':
        print(f"{cores['negritoroxo']}Computador VENCEU!{cores['limpa']}")
    else:
        print(f"{cores['negritoroxo']}EMPATE!{cores['limpa']}")

elif jogador == 'papel':

    if computador == 'pedra':
        print(f"{cores['negritoroxo']}Jogador VENCEU!{cores['limpa']}")
    elif computador == 'tesoura':
        print(f"{cores['negritoroxo']}Computador VENCEU!{cores['limpa']}")
    else:
        print(f"{cores['negritoroxo']}EMPATE!{cores['limpa']}")

else:

    if computador == 'papel':
        print(f"{cores['negritoroxo']}Jogador VENCEU!{cores['limpa']}")
    elif computador == 'pedra':
        print(f"{cores['negritoroxo']}Computador VENCEU!{cores['limpa']}")
    else:
        print(f"{cores['negritoroxo']}EMPATE!{cores['limpa']}")
# ------------------------------------------------------------| Desafio [045]
