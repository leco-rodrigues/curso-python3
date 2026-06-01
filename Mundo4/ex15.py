"""
Coloque nos comentários a estrutura de dois objetos:
um concreto e outro abstrato.
Inclua também seus principais atributos, métodos e
crie um exemplo de estado para cada um deles.
"""

from utils.strings import exit_message, display_message_box
from utils.colors import text_color

# Passo 1: Estruturar um objeto concreto
""" 
Nome da classe: Livro;
Atributos: [titulo, numero_paginas, cor, edicao, autor, usado, data_lancamento, tamanho, peso]
Métodos: [ler(), abrir(), fechar()]
"""
# Passo 2: Estruturar um objeto abstrato
"""
Nome da classe: Pensamento
Atributos: [conteudo, tipo, intensidade]
Métodos: [pensar(), refletir(), analisar()]
"""
# Passo 3: Criar um exemplo de estado para o objeto concreto
"""
titulo: "A Volta Dos Que Não Foram"
numero_paginas: 360
cor: "Marrom"
edicao: 1
autor: "Alex Rodrigues"
usado: False
data_lancamento: 2026
tamanho: "20x10cm"
peso: "1kg"
"""

# Passo 4: Criar um exemplo de estado para o objeto abstrato
"""
conteudo: "Preciso estudar Python hoje."
tipo: "Positivo"
intensidade: 8
"""

# Passo 5: Exibir uma mensagem de encerramento
display_message_box(text_color(exit_message(), "amarelo"))
# -------------------------------------------------------| AULA 03 - POO PARA INICIANTES: GUIA DEFINITIVO - CLASSES, OBJETOS, ATRIBUTOS, ETC | DESAFIO 15
