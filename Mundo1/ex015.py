# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

# Passo 1: Receber os valores para "Km" e "dias"
km = float(input('Quantos Km foram percorridos durante o aluguel? ')) # km percorridos
dias = int(input('Foram quantos dias de aluguel? ')) # dias de aluguel

# Passo 2: Calcular o preço do aluguel
print(f'Com base no tempo de aluguel e Km rodados, o preço ficou em R${(dias * 60) + (km * 0.15):.2f}.') # aluguel = (dia * 60) + (km * 0.15)
# ------------------------------------------------------------------------------------------------------------------ Desafio [015]
