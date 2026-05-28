"""
Na teoria de OO, o termo usado para o ato de fazer um objeto existir, a partir de um modelo se chama:

A - instanciar *
B - classificar
C - objetificar
D - forjar
"""

from utils.strings import exit_message, display_message_box
from utils.colors import text_color
from perguntas import pergunta

# Passo 1: Responder à pergunta
pergunta("Na teoria de OO, o termo usado para o ato de fazer um objeto existir a partir de um modelo se chama:",
         "instanciar", "classificar", "objetificar", "forjar", "A")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 03 - POO PARA INICIANTES: GUIA DEFINITIVO - CLASSES, OBJETOS, ATRIBUTOS, ETC | DESAFIO 12
