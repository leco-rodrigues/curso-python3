# Formatando Moedas em Python:
    # Adapte o código do desafio 107,
    # criando uma função adicional chamada moeda() que consiga mostrar
    # os valores como um valor monetário formatado.

from utils.strings import exit_message, display_message_box
# Passo 1: Criar função adicional
from utils import numbers

# Passo 2: Exibir o resultado
valor: float = float(input("Digite um valor: R$"))
aumento: float = float(input("Deseja um aumento de quantos %? "))
desconto: float = float(input("Deseja um desconto de quantos %? "))

valor_dobro: float = numbers.dobro(valor)
valor_metade: float = numbers.metade(valor)
valor_aumentado: float = numbers.aumentar(valor, desconto)
valor_descontado: float = numbers.diminuir(valor, desconto)

print(f"O dobro de {numbers.moeda(valor)} é igual a {numbers.moeda(valor_dobro)}.")
print(f"A metade de {numbers.moeda(valor)} é igual a {numbers.moeda(valor_metade)}.")
print(f"Um aumento de {aumento}% sobre {numbers.moeda(valor)} é igual a {numbers.moeda(valor_aumentado)}.")
print(f"Um desconto de {desconto}% sobre {numbers.moeda(valor)} é igual a {numbers.moeda(valor_descontado)}.")

# Passo 3: Exibir uma mensagem de encerramento
display_message_box(exit_message())
# --------------------------------| AULA 22 - MÓDULOS E PACOTES | DESAFIO [108]
