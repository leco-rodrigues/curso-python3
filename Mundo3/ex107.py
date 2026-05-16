# Exercitando módulos em Python:
    # Crie um módulo chamado moeda.py que tenha as funções incorporadas
    # aumentar(), diminuir(), dobro() e metade().
    # Faça também um programa que importe esse módulo e use algumas dessas funções.

from utils.strings import exit_message, display_message_box
# Passo 1: Criar um módulo com funções
from utils import numbers

# Passo 2: Criar um programa que utilize essas funções
valor: float = float(input("Digite um valor: R$"))
aumento: float = float(input("Deseja um aumento de quantos %? "))
desconto: float = float(input("Deseja um desconto de quantos %? "))

valor_dobro: float = numbers.dobro(valor)
valor_metade: float = numbers.metade(valor)
valor_aumentado: float = numbers.aumentar(valor, desconto)
valor_descontado: float = numbers.diminuir(valor, desconto)

# Passo 3: Exibir o resultado
print(f"O dobro de {valor} é igual a {valor_dobro}.")
print(f"A metade de {valor} é igual a {valor_metade}.")
print(f"Um aumento de {aumento}% sobre {valor} é igual a {valor_aumentado}.")
print(f"Um desconto de {desconto}% sobre {valor} é igual a {valor_descontado}.")

# Passo 4: Exibir uma mensagem de encerramento
display_message_box(exit_message())
# --------------------------------| AULA 22 - MÓDULOS E PACOTES | DESAFIO [107]
