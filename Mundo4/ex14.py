"""
Ao conjunto de todos os valores de atributos de um objeto em um determinado momento, damos o nome de:

A - identidade
B - instância
C - método
D - estado *
"""

from utils.strings import exit_message, display_message_box
from utils.colors import text_color
from perguntas import pergunta

# Passo 1: Responder à pergunta

pergunta("Ao conjunto de todos os valores de atributos de um objeto em um determinado momento, damos o nome de:",
         "identidade", "instância", "método", "estado", "D")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 03 - POO PARA INICIANTES: GUIA DEFINITIVO - CLASSES, OBJETOS, ATRIBUTOS, ETC | DESAFIO 14
