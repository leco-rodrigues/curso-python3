"""
A linguagem Simula foi um superconjunto de que outra linguagem?

A - ALGOL *
B - C
C - SmallTalk
D - Python
"""

from utils.strings import exit_message, display_message_box
from utils.colors import text_color
from perguntas import pergunta

# Passo 1: Responder à pergunta
pergunta("A linguagem Simula foi um superconjunto de que outra linguagem?", "ALGOL", "C", "SmallTalk", "Python", "A")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 01 - CRISE DO SOFTWARE: O MOTIVO DO SURGIMENTO DA POO | DESAFIO 04
