# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R%0.15 por Km rodado.

# Passo 1: Receber os valores de "Km percorridos", "dias de aluguel"
km = float(input('Quantos Km foram percorridos durante o aluguel? '))
dias = int(input('Foram quantos dias de alguel? '))

# Passo 2: Calcular o preço a ser pago com base nesses valores ((dia * 60) + (km * 0.15))
print(f'Com base no tempo de aluguel e Km rodados, o preço do aluguel ficou por R${(dias * 60) + (km * 0.15):.2f}.')
# --------------------------------------------------------------------------------------------------------- Desafio [015]
