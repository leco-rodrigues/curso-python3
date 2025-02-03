# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere: US$1.00 = R$3.27

# Passo 1: Receber um valor de "dinheiro"
dinheiro = float(input('Quanto dinheiro você tem na carteira? '))

# Passo 2: Calcular quantos dólares é possível comprar com esse valor (dinheiro / 3.27)
print(f'Com R${dinheiro:.2f} é possível comprar US${dinheiro / 3.27}.')
# --------------------------------------------------------------------- Desafio [010]
