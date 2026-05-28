"""
Se precisar adicionar uma nova funcionalidade ao sistema,
consigo fazer isso com grande facilidade.

A - Natural
B - Extensível *
C - Reutilizável
D - Oportuno
"""

from utils.strings import exit_message, display_message_box
from utils.colors import text_color
from perguntas import pergunta

# Passo 1: Responder à pergunta
pergunta("Se precisar adicionar uma nova funcionalidade ao sistema, consigo fazer isso com grande facilidade.", "Natural", "Extensível", "Reutilizável", "Oportuno", "B")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 02 - AS 6 VANTAGENS DA POO: PROGRAMAÇÃO ORIENTADA A OBJETOS | DESAFIO 07
