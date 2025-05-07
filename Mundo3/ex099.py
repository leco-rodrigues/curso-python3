# Função que descobre o maior:
    # Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
    # Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def show_exit_message(message: str = None) -> None:
    if message is None:
        message = "Exiting program... Thanks for using it! 😄"
    show_formated_message(message, "-")


def show_error_message(message: str = None) -> None:
    if (not message):
        message = "Invalid input! Please check."
    show_formated_message(f"Invalid input: {message}", "-", 7, False)


def show_formated_message(text: str = None, sep: str = None, sep_multi: int = None, central: bool = True) -> None:
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


def yes_no(question: str = None) -> bool:
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
            show_error_message(f"{e}")

    if (choice in ("no", "n")):
        return False
    return True


# Passo 1: Criar função para mostrar o "maior valor" dentre todos os argumentos recebidos
def number_input(pergunta: str) -> tuple:
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
            show_error_message(f"{e}")
            continue

        if (not yes_no("Do you want to add another number to the list?")):
            return tuple(numbers_list)


def maior(*numeros: int) -> int:
    print(max(numeros))


# Passo 2: Exibir o "maior valor"
show_formated_message("EXIBINDO O MAIOR VALOR", "-")

maior(number_input("Enter a number:"))

# Passo 3: Exibir mensagem de encerramento:
show_exit_message()
# ----------------| AULA 21 - FUNÇÕES (PARTE 1) | DESAFIO [099]
