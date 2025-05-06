# Função de Contador:
    # Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
    # Seu programa tem que realizar três contagens através da função criada:
        # a) De 1 até 10, de 1 em 1
        # b) De 10 até 0, de 2 em 2
        # c) Uma contagem personalizada

from time import sleep


def show_exit_message(message: str = None) -> None:
    if (not message):
        message = "Exiting program... Thanks for using it! 😄"
    escreva(message, "-")


def exibir_mensagem_erro(mensagem: str = None) -> None:
    if (not mensagem):
        mensagem = "Por favor, preencha o campo corretamente."
    escreva(f"Entrada inválida: {mensagem}", "-", 7, False)


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


# Passo 1: Criar função para um "contador" a partir do "inicio", "fim" e "passo"
def contagem_input(pergunta: str = None) -> int:
    prompt: str = pergunta.strip() + " "

    while True:
        try:
            valor: str = str(input(prompt))
            if (not valor.strip()):
                raise ValueError("O campo está vazio. Por favor, preencha-o com um número inteiro.")

            valor_formatado: str = valor.strip().lstrip("-")

            if (valor_formatado.isdigit()):
                valor_formatado = int(valor_formatado)

            if (not isinstance(valor_formatado, int)):
                raise ValueError(f"O valor '{valor_formatado}' não é válido. Por favor, insira um número inteiro.")

            return int(valor)
        except ValueError as e:
            escreva(f"Entrada inválida: {e}", "-", 7, False)


def validar_fim(inicio: int, fim:int) -> bool:
    if (inicio == fim):
        exibir_mensagem_erro("Os valores de 'início' e 'fim' da contagem não podem ser iguais.")
        return False
    return True


def validar_passo(inicio: int, fim: int, passo: int) -> bool:
    if (passo == 0):
        exibir_mensagem_erro("O valor de 'passo' da contagem não pode ser igual a 0.")
        return False
    soma_abs: int = abs(inicio) + abs(fim)
    if (passo > soma_abs):
        exibir_mensagem_erro(f"O valor de 'passo' da contagem não pode ser maior que o valor absoluto da soma de 'início' e 'fim' dela (ex.: {abs(inicio)} + {abs(fim)} = {soma_abs}).")
        return False
    return True


def ajustar_passo(inicio: int, fim: int, passo: int) -> int:
    if ((inicio > fim) and (passo > 0)) or ((inicio < fim) and (passo < 0)):
        escreva(f"O valor de 'passo' da contagem foi ajustado para que ela ocorra devidamente ({passo} * -1 = {passo * -1}).", "-", "7", False)
        sleep(1.5)
        return -passo
    return passo

def exibir_contagem(inicio: int, fim: int, passo: int) -> None:
    fim_real: int = fim + ((1) if (inicio < fim) else (-1))
    for n in range(inicio, fim_real, passo):
        print(n, end = " -> ", flush = True)
        sleep((abs(passo)) if (n != fim) else (0))
    print("FIM")


def contador(inicio: int = None, fim: int = None, passo: int = None) -> None:
    if (inicio is None) or (fim is None) or (passo is None):
        escreva("MONTANDO A CONTAGEM", "-")

        if (inicio is None):
            inicio = contagem_input("\n-------\nDigite o valor inicial da contagem:")

        if (fim is None):
            while True:
                fim = contagem_input("\n-------\nDigite o valor final da contagem:")

                if (not validar_fim(inicio, fim)):
                    continue

                break

        if (passo is None):
            while True:
                passo = contagem_input("\n-------\nDigite o valor dos passos da contagem:")

                if (not validar_passo(inicio, fim, passo)):
                    continue

                break

    if (not validar_fim(inicio, fim)):
        return

    escreva((("CONTAGEM PROGRESSIVA") if (inicio < fim) else ("CONTAGEM REGRESSIVA")), "-")

    if (not validar_passo(inicio, fim, passo)):
        return

    passo = ajustar_passo(inicio, fim, passo)

    exibir_contagem(inicio, fim, passo)

# Passo 2: Exibir "contagem progressiva" (1, 10, 1)
contador(10, 1, 1)

# Passo 3: Exibir "contagem regressiva" (10, 0, 2)
contador(10, 0, 2)

# Passo 4: Exibir "contagem personalizada"
contador()

# Passo 5: Exibir mensagem de encerramento:
show_exit_message()
# ----------------| AULA 21 - FUNÇÕES (PARTE 1) | DESAFIO [098]
