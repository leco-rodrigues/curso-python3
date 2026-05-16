# Transformando módulos em pacotes
    # Crie um pacote chamado utilidadesCeV que tenha dois módulos internos
    # chamados moeda e dado.
    # Transfira todas as funções utilizadas nos desafios 107, 108 e 109
    # para o primeiro pacote e mantenha tudo funcionando.

from utils.strings import exit_message, display_message_box
# Passo 1: Criar um pacote e transferir todas as funções
from utils import numbers

# Passo 2: Exibir o resultado
valor: float = float(input("Digite um valor: R$"))
aumento: float = float(input("Digite a porcentagem de aumento: "))
desconto: float = float(input("Digite a porcentagem de desconto: "))

print(f"O dobro de {numbers.moeda(valor)} é igual a {numbers.dobro(valor, True)}.")
print(f"A metade de {numbers.moeda(valor)} é igual a {numbers.metade(valor, True)}.")
print(f"Um aumento de {aumento}% sobre {numbers.moeda(valor)} é igual a {numbers.aumentar(valor, aumento, True)}.")
print(f"Um desconto de {desconto}% sobre {numbers.moeda(valor)} é igual a {numbers.diminuir(valor, desconto, True)}.")

numbers.resumo(valor, aumento, desconto)

# Passo 3: Exibir uma mensagem de encerramento
display_message_box(exit_message())
# # ------------------------------| AULA 22 - MÓDULOS E PACOTES | DESAFIO [111]
