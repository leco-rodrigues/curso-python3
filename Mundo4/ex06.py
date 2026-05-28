"""
Criei um sistema para Escola, ao criar outro sistema para Academia,
parte do trabalho já estará feito, pois tenho Alunos nos dois.

A - Confiável
B - Natural
C - Manutenível
D - Reutilizável *
"""

from utils.strings import exit_message, display_message_box
from utils.colors import text_color
from perguntas import pergunta

# Passo 1: Responder à pergunta
pergunta("Criei um sistema para Escola, ao criar outro sistema para Academia, parte do trabalho já estará feito, pois tenho Alunos nos dois.", 
         "Confiável", "Natural", "Manutenível", "Reutilizável", "D")

# Passo 2: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 02 - AS 6 VANTAGENS DA POO: PROGRAMAÇÃO ORIENTADA A OBJETOS | DESAFIO 06
