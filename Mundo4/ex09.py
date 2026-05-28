"""
O código fica muito simples de ler e de compreender,
já que não preciso saber os detalhes de funcionamento ao programar.

A - Natural *
B - Extensível
C - Manutenível
D - Oportuno
"""

from utils.strings import exit_message, display_message_box
from utils.colors import text_color
from perguntas import pergunta

# Passo 1: Responder à pergunta
pergunta("O código fica muito simples de ler e de compreender, já que não preciso saber os detalhes de funcionamento ao programar.",
         "Natural", "Extensível", "Manutenível", "Oportuno", "A")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 02 - AS 6 VANTAGENS DA POO: PROGRAMAÇÃO ORIENTADA A OBJETOS | DESAFIO 06
