# Formatando Moedas em Python
    # Modifique as funções que foram criadas no desafio 107 para que elas aceitem
    # um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
    # formatado pela função moeda(), desenvolvida no desafio 108.

from utils.strings import exit_message, display_message_box
# Passo 1: Modificar as funções
from utils import numbers

valor: float = float(input("Digite um valor: R$"))
aumento: float = float(input("Digite a porcentagem de aumento: "))
desconto: float = float(input("Digite a porcentagem de desconto: "))

# Passo 2: Exibir o resultado
print(f"O dobro de {numbers.moeda(valor)} é igual a {numbers.dobro(valor, True)}.")
print(f"A metade de {numbers.moeda(valor)} é igual a {numbers.metade(valor, True)}.")
print(f"Um aumento de {aumento}% sobre {numbers.moeda(valor)} é igual a {numbers.aumentar(valor, aumento, True)}.")
print(f"Um desconto de {desconto}% sobre {numbers.moeda(valor)} é igual a {numbers.diminuir(valor, desconto, True)}.")

# Passo 3: Exibir uma mensagem de encerramento
display_message_box(exit_message())
# --------------------------------| AULA 22 - MÓDULOS E PACOTES | DESAFIO [109]
