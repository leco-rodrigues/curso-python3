"""
Eu posso alterar como uma funcionalidade trabalha e
tudo continua funcionando como antes.

A - Oportuno
B - Reutilizável
C - Confiável *
D - Natural
"""

from utils.strings import exit_message, display_message_box
from utils.colors import text_color
from perguntas import pergunta

# Passo 1: Responder à pergunta
pergunta("Eu posso alterar como uma funcionalidade trabalha e tudo continua funcionando como antes.", "Oportuno", "Reutilizável", "Confiável", "Natural", "C")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 02 - AS 6 VANTAGENS DA POO: PROGRAMAÇÃO ORIENTADA A OBJETOS | DESAFIO 10
