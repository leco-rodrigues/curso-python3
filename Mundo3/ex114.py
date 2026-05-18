# Site está acessível?:
    # Crie um código em Python que teste se o site pudim está acessível
    # pelo computador usado.

from utils.strings import exit_message, display_message_box
import urllib.request
import urllib.error

# Passo 1: Criar código
try:
    requisicao = urllib.request.Request(
        "https://pudim.com.br",
        headers={"User-Agent": "Edg/124.0.0.0"}
    )
    site = urllib.request.urlopen(requisicao, timeout = 5)
except urllib.error.URLError:
    print("O site Pudim não está acessível no momento.")
else:
    print("O site Pudim se encontra acessível no momento.")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(exit_message())
# --------------------------------| AULA 23 - TRATAMENTO DE ERROS E EXCEÇÕES | DESAFIO [114]
