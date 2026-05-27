"""
Em que década aconteceu a "Crise do Software" no mercado?

A - 1950
B - 1960 *
C - 1980
D - 2000
"""

from utils.strings import exit_message, display_message_box
from utils.colors import text_color
from perguntas import pergunta

# Passo 1: Responder à pergunta
pergunta("Em que década aconteceu a 'Crise do Software' no mercado?", "1950", "1960", "1980", "2000", "B")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 01 - CRISE DO SOFTWARE: O MOTIVO DO SURGIMENTO DA POO | DESAFIO 01
