# Funções para votação:
    # Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from datetime import datetime


def display_exit_message(message: str = None) -> None:
    if (not message):
        message = "Exiting program... Thanks for using it! 😄"
    print(message)


# Passo 1: Criar uma função indicando a situação eleitoral com base no ano de nascimento da pessoa
def voto(ano_nasc: int = int(input("Digite o ano de nascimento: "))) -> None:
    idade: int = datetime.now().year - ano_nasc
    if idade >= 18 and idade < 71:
        print(f"Com {idade} anos: Voto OBRIGATÓRIO")
    elif 16 <= idade < 18 and idade > 70:
        print(f"Com {idade} anos: Voto OPCIONAL")
    else:
        print(f"Com {idade} anos: Voto NEGADO")


# Passo 2: Exibir o resultado
voto()

# Passo 3: Exibir mensagem de encerramento
display_exit_message()
# -------------------| AULA 21 - FUNÇÕES (PARTE 2) | DESAFIO [101]
