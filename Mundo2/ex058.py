# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from custom_module import txt_style as styl, sepa_rator as sep_
from random import randint
from time import sleep


# Passo 1: Solicitar valores para "número" e "palpite"
print(styl(f"\t{' GUESS THE NUMBER ':=^40}\n", 'bd'))

print(styl("Please wait while the computer is processing a number between 0 and 10...\n", 'bd'))

sleep(1.5)

num: int = randint(0, 10)
cont: int = 0

while True:
    print(sep_(color = 'c'))
    palpite: int = int(input(styl("Guess the number:", 'n') + " "))
    cont += 1
    print(sep_(color = 'c'))

    if palpite == num:
        print(styl(f'You guessed it! Congratulations! The drawn number was {num}.', 'bd', 'g'))
        break

    elif palpite < num:
        print(styl("The number is higher... Please try again.", 'bd', 'y'))

    elif palpite > num:
        print(styl("The number is lower... Please try again.", 'bd', 'b'))

# Passo 2: Exibir número de tentativas
print(sep_(color = 'c'))
print(styl(f'Number of attempts: {cont}', 'bd', 'p'))

print(sep_(color = 'c'))
print(styl("END", 'bd'))
# ---------------------| Desafio [058]
