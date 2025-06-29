# Função para fatorial:
    # Crie um programa que tenha uma função chamada fatorial() que receba dois parâmetros:
    # o primeiro que indique o número a calcular e o outro chamado show,
    # que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def display_exit_message(message: str = None) -> None:
    if (not message):
        message = "Exiting program... Thanks for using it! 😄"
    print(message)


# Passo 1: Criar função que calcule o fatorial de um número
def fatorial(numero: int = int(input("Digite um número para fatorar: ")), show = False) -> None:
    fatorial: int = 1
    for contador in range(numero, 0, -1):
        fatorial *= contador
        if show:
            print(f"{contador} {'x ' if contador > 1 else "= "}", end = "", flush = True)
    print(fatorial)

# Passo 2: Exibir o resultado
fatorial()

# Passo : Exibir mensagem de encerramento
display_exit_message()
# -------------------| AULA 21 - FUNÇÕES (PARTE 2) | DESAFIO [102]
