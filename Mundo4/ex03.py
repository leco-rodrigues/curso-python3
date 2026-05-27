"""
Quem foi o criador da linguagem SmallTalk, umas das primeiras linguagens OO?

A - Edsger Dijkstra
B - Guido Van Rossum
C - Alan Kay *
D - Kristen Nygaard
"""

from utils.strings import exit_message, display_message_box
from utils.colors import text_color
from perguntas import pergunta

# Passo 1: Responder à pergunta
pergunta("Quem foi o criador da linguagem SmallTalk, umas das primeiras linguagens OO?",
         "Edsger Dijkstra", "Guido Van Rossum", "Alan Kay", "Kristen Nygaard", "C")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 01 - CRISE DO SOFTWARE: O MOTIVO DO SURGIMENTO DA POO | DESAFIO 03
