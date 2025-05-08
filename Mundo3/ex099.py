# Função que descobre o maior:
    # Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
    # Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def display_exit_message(message: str = None) -> None:
    if message is None:
        message = "Exiting program... Thanks for using it! 😄"
    display_message_box(message, "-")


def display_error(message: str = None) -> None:
    if (not message):
        message = "Invalid input! Please check."
    display_message_box(f"Invalid input: {message}", "-", 7, False)


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


def prompt_yes_no(question: str = None) -> bool:
    if (not question):
        question = "Do you want to continue? (y/n)"

    prompt: str = "\n----------\n" + question.strip() + " "

    while True:
        try:
            choice: str = str(input(prompt)).strip().lower()

            if (choice not in ("yes", "y", "no", "n")):
                raise ValueError("Please enter 'yes'/'y' or 'no'/'n'.")

            break
        except ValueError as e:
            display_error(f"{e}")

    if (choice in ("no", "n")):
        return False
    return True


# Passo 1: Criar função para mostrar o "maior valor" dentre todos os argumentos recebidos
def collect_integers(pergunta: str) -> tuple:
    prompt: str = "\n-------\n" + pergunta.strip() + " "
    numbers_list: list[int] = []

    while True:
        try:
            numero: str = str(input(prompt))

            if (not numero):
                raise ValueError("Empty space is not allowed. Please enter a whole number.")

            numero_formatado: str = numero.lstrip("-")

            if (numero_formatado.isdigit()):
                numero_formatado = int(numero_formatado)

            if (not isinstance(numero_formatado, int)):
                raise ValueError(f"The value '{numero_formatado}' is invalid. Please enter a whole number.")

            numbers_list.append(int(numero))
        except ValueError as e:
            display_error(f"{e}")
            continue

        if (not prompt_yes_no("Do you want to add another number to the list?")):
            return tuple(numbers_list)


def maior(*numeros: int) -> int:
    num_maior: int | None = None
    count: int = 0

    if (not numeros):
        if (not prompt_yes_no("Deseja adicionar números para análise? (y/n)")):
            display_message_box("Não há números para serem analisados", "-", 7, False)
            return
        numeros = collect_integers("Digite um número para análise:")

    display_message_box("Analisando os números...", "-", 7, False)

    for n in numeros:
        print(n, end = " | ", flush = True)
        if (num_maior is None) or (n > num_maior):
            num_maior = n
        count += 1
        sleep(1)

    print("FIM")
    sleep(1)
    display_message_box(f"Quantidade de valores analisados: {count} \nMaior valor apresentado: {num_maior}", "-", 7, False)


# Passo 2: Exibir o "maior valor"
display_message_box("EXIBIR O MAIOR VALOR", "-")

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()

# Passo 3: Exibir mensagem de encerramento:
display_exit_message()
# ----------------| AULA 21 - FUNÇÕES (PARTE 1) | DESAFIO [099]
