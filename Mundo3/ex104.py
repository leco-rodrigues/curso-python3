# Validando entrada de dados uem Python:
    # Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
    # só que fazendo a validação para aceitar apenas um valor numérico.
    # Ex:
        # n = leiaInt('Digite um n')

def display_exit_message(message: str = None) -> None:
    if (not message):
        message = "Exiting program... Thanks for using it! 😄"
    print(message)


# Passo 1: Criar uma função chamada "leiaInt()" que aceite apenas valores numéricos
def leiaInt(pergunta: str = "Digite um número:") -> int:
    prompt: str = pergunta.strip() + " "
    while True:
        numero: str = str(input(prompt))
        if numero.isdigit():
            return numero
        print("ERRO! Por favor, digite um número inteiro.")


# Passo 2: Exibir o resultado
n: int = leiaInt("Digite um número:")
print(f"Você digitou o número {n}.")

# Passo 3: Exibir mensagem de encerramento
display_exit_message()
# -------------------| AULA 21 - FUNÇÕES (PARTE 2) | DESAFIO [104]
