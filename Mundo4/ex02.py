"""
Qual das características a seguir identifica as primeiras linguagens lineares?

A - Maior modularidade
B - Desvios forçados com GOTO *
C - Estruturas de controle
D - Instruções de baixo nível
"""
from utils.strings import exit_message, display_message_box
from utils.colors import text_color
from perguntas import pergunta

# Passo 1: Responder à pergunta
pergunta("Qual das características a seguir identifica as primeiras linguagens lineares?",
         "Maior modularidade", "Desvios forçados com GOTO", "Estruturas de ocntrole", "Instruções de baixo nível", "B")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 01 - CRISE DO SOFTWARE: O MOTIVO DO SURGIMENTO DA POO | DESAFIO 02
