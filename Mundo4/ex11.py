"""
Qual dos objetos abaixo seria o único abstrato da lista?

A - Sensor
B - Robô
C - Notificação *
D - Livro
"""

from utils.strings import exit_message, display_message_box
from utils.colors import text_color
from perguntas import pergunta

# Passo 1: Responder à pergunta
pergunta("Qual dos objetos abaixo seria o único abstrato da lista?", "Sensor", "Robô", "Notificação", "Livro", "C")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 03 - POO PARA INICIANTES: GUIA DEFINITIVO - CLASSES, OBJETOS, ATRIBUTOS, ETC | DESAFIO 11
