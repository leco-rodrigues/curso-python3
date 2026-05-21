# Criando um menu em Python:
    # Crie um sistema modularizado que permita cadastrar pessoas pelo seu nome e
    # idade em um arquivo de texto simples.
    # O sistema só vai ter 2 opções: cadastrar uma nova pessoas e
    # listar todas as pessoas cadastradas.

from utils.strings import exit_message, display_message_box, error_message
from utils.colors import text_color
# Passo 1: Criar o sistema
import uteis

# Passo 2: Exibir o resultado
escolha: int = uteis.menu()

if escolha == 1:
    try:
        uteis.exibir_cadastros()
    except:
        error_message(text_color("ERRO: Arquivo não existe!", "vermelho"))

if escolha == 2:
    pessoa: dict[str, object] = uteis.cadastrar()
    nome: str = pessoa["nome"]
    idade: int = pessoa["idade"]

    uteis.adcionar_cadastro(nome, idade)

    display_message_box(text_color("Cadastro realizado com sucesso!", "verde"), sep_multi = 26)

# Passo 3: Exibir uma mensagem de encerramento
if escolha == 3:
    msg: str = exit_message("Saindo do programa")
    display_message_box(text_color(msg, "vermelho"), sep_multi = 26)
# -----------------------------------------------------------------| AULA 23 - TRTAMENTO DE ERROS E EXCEÇÕES | DESAFIO [115]
