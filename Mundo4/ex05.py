"""
Na sigla OOAD, as últimas duas letras significam...

A - Algol/Dashbord
B - Algorithms/Digital
C - Analytics/Default
D - Analysis/Design *
"""

from utils.strings import exit_message, display_message_box
from utils.colors import text_color
from perguntas import pergunta

# Passo 1: Responder à pergunta
pergunta("Na sigla OOAD, as últimas duas letras significam...",
         "Algol/Dashbord", "Algorithms/Digital", "Analytics/Default", "Analysis/Design", "D")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 01 - CRISE DO SOFTWARE: O MOTIVO DO SURGIMENTO DA POO | DESAFIO 05
