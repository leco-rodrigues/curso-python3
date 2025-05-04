# Um print especial:
    # Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
    # Ex:
        # escreva('Olá, Mundo!')
        # Saída:
        # ~~~~~~~~~~~
        # Olá, Mundo!
        # ~~~~~~~~~~~

def show_exit_message(message: str = None) -> None:
    if (message is None):
        message = "\n----------\nExiting program... Thanks for using it! 😄\n----------\n"
    print(message)


# Passo 1: Criar função para exibir uma "mensagem" com tamanho adaptável a partir de um "texto"
def escreva(text: str = None, sep: str = None) -> None:
    if (not text):
        text = "Olá, Mundo!"
    if (not sep):
        sep = "~"
    separador:str = sep * (len(text) + 4)
    message: str = f"\n{separador}\n  {text}\n{separador}\n"
    print(message)


# Passo 2: Exibir "mensagem"
escreva("Hello, World!", "-")

# Passo 3: Exibir mensagem de encerramento:
show_exit_message()
# ----------------| AULA 21 - FUNÇÕES (PARTE 1) | DESAFIO [097]
