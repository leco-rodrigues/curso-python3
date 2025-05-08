# Funções para sortear e somar:
    # Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
    # A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint
from time import sleep


def display_exit_message(message: str = None) -> None:
    if message is None:
        message = "Exiting program... Thanks for using it! 😄"
    display_message_box(message, "-")


def display_message_box(text: str = None, sep: str = None, sep_multi: int = None, central: bool = True) -> None:
    if (not text):
        text = "Olá, Mundo!"
    if (not sep):
        sep = "~"
    if (not sep_multi):
        sep_multi = len(text) +4
    if (central):
        text = "  " + text
    separator: str = sep * int(sep_multi)
    message: str = f"\n{separator}\n{text}\n{separator}\n"
    print(message)


# Passo 1: Criar uma função que sorteia 5 números e os coloca dentro de uma lista
def sorteia() -> list:
    numbers_list: list[int] = [randint(1, 100) for _ in range(5)]
    return numbers_list


def display_list(numbers: list[int]) -> None:
    display_message_box("EXIBINDO A LISTA DE NÚMEROS", "-")

    for n in numbers:
        print(n, end = " | ", flush = True)
        sleep(1)
    print("FIM")
    sleep(1)


# Passo 2: Criar função que soma os pares dentre os números sorteados
def somaPar(random_int_list: list[int], pausar: bool = True) -> None:
    display_message_box("EXIBINDO OS PARES", "-")

    sumEven: int = 0
    count: int = 0

    for n in random_int_list:
        if (n % 2 == 0):
            print(n, end = " | ", flush = True)
            sumEven += n
            count += 1
            sleep(1)
    print("FIM\n")
    sleep(1)

    if (count == 0):
        display_message_box("Não há números pares para serem somados.", "-", 7, False)
        return

    if (count == 1):
        display_message_box(f"Houve apenas um número par: {sumEven}", "-", 7, False)
        return

    display_message_box(f"Soma dos pares: {sumEven}", "-", 7, False)


# Passo 3: Exibir a lista sorteada
random_numbers: list[int] = sorteia()
display_list(random_numbers)

# Passo 4: Exibir a soma dos pares
somaPar(random_numbers)
sleep(1)

# Passo 5: Exibir mensagem de encerramento:
display_exit_message()
# -------------------| AULA 21 - FUNÇÕES (PARTE 1) | DESAFIO [100]
