# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

# Passo 1: Receber valores para "Km" e "dias"
km = float(input('\033[7;40mQuantos Km foram percorridos durante o aluguel?\033[m '))
dias = int(input('\033[7;40mForam quantos dias de aluguel?\033[m '))

# Passo 2: Exibir o preço do aluguel
print(f'\033[1;34mCom base no tempo de aluguel e Km rodados, o preço da passagem ficou em R${(dias * 60) + (km * 0.15):.2f}.\033[m')
# -------------------------------------------------------------------------------------------------------------------------------------------------------| Desafio [015]
