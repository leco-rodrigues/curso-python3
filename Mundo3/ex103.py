# Ficha do jogador:
    # Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
    # o nome de um jogador e quantos gols ele marcou.
    # O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def display_exit_message(message: str = None) -> None:
    if (not message):
        message = "Exiting program... Thanks for using it! 😄"
    print(message)


# Passo 1: Criar função chamada ficha que exiba a ficha de um jogador
def ficha(jogador: str = "<desconhecido>", gols: int = 0) -> None:
    print(f"O jogador {jogador} marcou {gols} gols.")


# Passo 2: Exibir o resultado
ficha()

# Passo 3: Exibir mensagem de encerramento
display_exit_message()
# -------------------| AULA 21 - FUNÇÕES (PARTE 2) | DESAFIO [103]
