# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from modulo import txt_style as styl, sep
from random import randint
from time import sleep


# Passo 1: Receber valores para "número" e "palpite"
print(styl(sep(7), color_ = 'c'), end = " ")
print(styl("ADIVINHE O NÚMERO", 'bd', 'p'), end = " ")
print(styl(sep(7), color_ = 'c'))

print(styl("\nAguarde enquanto o computador está processando um número aleatório entre 0 e 10...\n", 'bd', 'p'))
sleep(1.5)

num: int = randint(0, 10)
cont: int = 0

while True:
    palpite: int = int(input(styl("Qual foi o número sorteado?", 'n') + " "))
    cont += 1

    if palpite == num:
        break

    print(styl("\nVocê errou! Por favor, tente novamente.", 'bd', 'r'))
    print(styl(sep(16), color_ = 'c'))

# Passo 2: Exibir número de tentativas
print(styl(sep(16), color_ = 'c'))
print(styl(f'Parabéns! Você acertou! O número correto era {num}.', 'bd', 'p'))
print(styl(f'Número de tentativas: {cont}', 'bd', 'b'))
# ---------------------------------------------------------| Desafio [058]
