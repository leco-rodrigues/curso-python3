# Entrada de dados monetários
    # Dentro do pacote utilidadesCeV que criamos no desafio 111,
    # temos um módulo chamado dado.
    # Crie uma função chamada leiaDinheiro que seja capaz de funcionar
    # como a função input(), mas com uma validação de dados para aceitar
    # apenas valores que sejam monetários.

from utils.strings import exit_message, display_message_box
# Passo 1: Criar a função
from utils.numbers import resumo, leiaDinheiro

valor: float = leiaDinheiro()

# Passo 2: Exibir o resultado
resumo(valor, 10, 50)

# Passo 3: Exibir uma mensagem de encerramento
display_message_box(exit_message())
# --------------------------------| AULA 22 - MÓDULOS E PACOTES | DESAFIO [112]
