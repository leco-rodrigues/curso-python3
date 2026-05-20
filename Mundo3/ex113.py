# Funções aprofundadas em Python:
    # Reescreva a função leiaInt() que fizemos no desafio 104,
    # incluindo agora a possibilidade da digitação de um número de tipo inválido.
    # Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from utils.strings import exit_message, display_message_box

# Passo 1: Reescrever a função leiaInt()
from utils.numbers import leiaInt

# Passo 2: Criar função leiaFloat()
from utils.numbers import leiaFloat

# Passo 3: Exibir o resultado
n_inteiro = leiaInt()
n_decimal = leiaFloat()

display_message_box(f"O número inteiro digitado foi {n_inteiro} e o número real foi {n_decimal:.2f}.", central = False)

# Passo 4: Exibir uma mensagem de encerramento
display_message_box(exit_message())
# --------------------------------| AULA 23 - TRATAMENTO DE ERROS E EXCEÇÕES | DESAFIO [113]
