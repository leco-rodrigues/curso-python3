# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}
# Passo 1: Receber valores para "Km" e "dias"
km = float(input(f'{cores['pretoebranco']}Quantos Km foram percorridos durante o aluguel?{cores['limpa']} ')) # km percorridos
dias = int(input(f'{cores['pretoebranco']}Foram quantos dias de aluguel?{cores["limpa"]} ')) # dias de aluguel

# Passo 2: Calcular e exibir o preço do aluguel
print(f'{cores['negritoazul']}Com base no tempo de aluguel e Km rodados, o preço da passagem ficou em R${(dias * 60) + (km * 0.15):.2f}.{cores['limpa']}') # aluguel = (dia * 60) + (km * 0.15)
# -------------------------------------------------------------------------------------------------------------------------------------------------------| Desafio [015]
