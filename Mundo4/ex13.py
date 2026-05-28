"""
Todo objeto tem uma lista de atividades que podem ser feitas com ele ou que ele pode desempenhar sozinho, que são:

A - atributos
B - métodos *
C - classes
D - instâncias
"""

from utils.strings import exit_message, display_message_box
from utils.colors import text_color
from perguntas import pergunta

# Passo 1: Responder à pergunta
pergunta("Todo objeto tem uma lista de atividades que podem se feitas com ele ou que ele pode desmepenhar sozinho, que são:",
         "atributos", "métodos", "classes", "instâncias", "B")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 03 - POO PARA INICIANTES: GUIA DEFINITIVO - CLASSES, OBJETOS, ATRIBUTOS, ETC | DESAFIO 13
