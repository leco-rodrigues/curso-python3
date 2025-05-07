# Funções para sortear e somar:
    # Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
    # A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

def show_exit_message(message: str = None) -> None:
    if message is None:
        message = "Exiting program... Thanks for using it! 😄"
    escreva(message, "-")


def escreva(text: str = None, sep: str = None, sep_multi: int = None, central: bool = True) -> None:
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


# Passo 1: 


# Passo : Exibir mensagem de encerramento:
show_exit_message()
# ----------------| AULA 21 - FUNÇÕES (PARTE 1) | DESAFIO [100]
