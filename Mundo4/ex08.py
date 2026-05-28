"""
Posso desenvolver várias funções que dependem uma da outra ao mesmo tempo
se o planejamento for seguido.

A - Oportuno *
B - Reutilizável
C - Confiável
D - Manutenível
"""

from utils.strings import exit_message, display_message_box
from utils.colors import text_color
from perguntas import pergunta

# Passo 1: Responder à pergunta
pergunta("Posso desenvolver várias funções que dependem uma da outra ao mesmo tempo se o planejamento for seguido.", "Oportuno", "Reutilizável", "Confiável", "Manutenível", "A")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 02 - AS 6 VANTAGENS DA POO: PROGRAMAÇÃO ORIENTADA A OBJETOS | DESAFIO 08
