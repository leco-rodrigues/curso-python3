# Exercitando módulos em Python:
    # Crie um módulo chamado moeda.py que tenha as funções incorporadas
    # aumentar(), diminuir(), dobro() e metade().
    # Faça também um programa que importe esse módulo e use algumas dessas funções.

from utils.strings import exit_message, display_message_box
# Passo 1: Criar um módulo com funções
from utils import numbers

# Passo 2: Criar um programa que utilize essas funções
salario: float = 1500
salario_dobro: float = numbers.dobro(salario)
salario_metade: float = numbers.metade(salario)
salario_aumentado: float = numbers.aumentar(salario, 50)
salario_diminuido: float = numbers.diminuir(salario, 50)

# Passo 3: Exibir o resultado
print(f"O dobro do seu salário de R${salario:.2f} é igual a R${salario_dobro:.2f}")
print(f"A metade do seu salário de R${salario:.2f} é igual a R${salario_metade:.2f}")
print(f"O aumento de 50% no seu salário de R${salario:.2f} é igual a R${salario_aumentado:.2f}")
print(f"A diminuição de 50% no seu salário de R${salario:.2f} é igual a R${salario_diminuido:.2f}")

# Passo 4: Exibir uma mensagem de encerramento
display_message_box(exit_message(), sep = "-")
# -------------------------------------------| AULA 22 - MÓDULOS E PACOTES | DESAFIO [107]
