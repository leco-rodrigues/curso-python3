# Interactive helping system in Python:
    # Faça um mini-sistema que utilize o Interactive Help do Python.
    # O usuário vai digitar o comando e o manual vai aparecer.
    # Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
    # OBS: use cores.

from time import sleep

def display_exit_message(message: str = None) -> None:
    if (not message):
        message = "Exiting program... Thanks for using it! 😄"
    print(message)

# Passo 1: Criar função que faça uso do Interactive Help do Python
def ihs_python(pergunta: str = "Função ou Biblioteca: ") -> None:
    print("\n----------\nSISTEMA dE AJUDA PyHELP\n----------\n")
    
    prompt: str = pergunta.strip() + " "
    while True:
        funcao_biblioteca: str = str(input(f"\n----------\n{prompt}\n----------\n")).strip()
        if funcao_biblioteca.lower() == "fim":
            print("\n----------\nVocê escolheu sair.\n----------\n")
            break
        print(f"\n----------\nACESSANDO O MANUAL DO COMANDO '{funcao_biblioteca}'\n----------\n")
        sleep(1)
        help(funcao_biblioteca)

# Passo 2: Exibir o resultado
ihs_python()

# Passo 3: Exibir mensagem de encerramento
display_exit_message()
# -------------------| AULA 21 - FUNÇÕES (PARTE 2) | DESAFIO [106]
