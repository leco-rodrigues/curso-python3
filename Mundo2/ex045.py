# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep


cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;100m', 'negritoroxo':'\033[1;35m', 'negritociano':'\033[1;36m'}

# Passo 1: Receber valores para "jogador1" e "jogador2"
escolhas = {1:'pedra', 2:'papel', 3:'tesoura'}
jogador = int(input(f"{cores['pretoebranco']}Jogador, escolha 'pedra', 'papel' ou 'tesoura':{cores['limpa']} "))
computador = f'{escolhas[randint(1, 3)]}'

# Passo 2: Exibir o resultado
print(f"{cores['negritociano']}-={cores['limpa']}" * 10)

print(f"{cores['negritociano']}JO{cores['limpa']}")
sleep(1)
print(f"{cores['negritociano']}KEN{cores['limpa']}")
sleep(1)
print(f"{cores['negritociano']}PÔ!{cores['limpa']}")
sleep(0.5)

print(f"{cores['negritociano']}-={cores['limpa']}" * 10)

print(f"{cores['negritoroxo']}Jogador: {escolhas[jogador]}{cores['limpa']}")
print(f"{cores['negritoroxo']}Computador: {computador}{cores['limpa']}")

print(f"{cores['negritociano']}-={cores['limpa']}" * 10)

if jogador == 1:
    
    if computador == 'tesoura':
        print(f"{cores['negritoroxo']}Jogador VENCEU!{cores['limpa']}")
    elif computador == 'papel':
        print(f"{cores['negritoroxo']}Computador VENCEU!{cores['limpa']}")
    else:
        print(f"{cores['negritoroxo']}Houve um EMPATE!{cores['limpa']}")

elif jogador == 2:

    if computador == 'pedra':
        print(f"{cores['negritoroxo']}Jogador VENCEU!{cores['limpa']}")
    elif computador == 'tesoura':
        print(f"{cores['negritoroxo']}Computador VENCEU!{cores['limpa']}")
    else:
        print(f"{cores['negritoroxo']}Houve um EMPATE!{cores['limpa']}")

elif jogador == 3:

    if computador == 'papel':
        print(f"{cores['negritoroxo']}Jogador VENCEU!{cores['limpa']}")
    elif computador == 'pedra':
        print(f"{cores['negritoroxo']}Computador VENCEU!{cores['limpa']}")
    else:
        print(f"{cores['negritoroxo']}Houve um EMPATE!{cores['limpa']}")

else:
    print(f"{cores['negritoroxo']}Opção INVÁLIDA!{cores['limpa']}")
# ----------------------------------------------------------------| Desafio [045]
