# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere: US$1.00 = R$3.27

# Passo 1: Receber um valor de "dinheiro"
dinheiro = float(input('Quantos reais você tem na carteira? '))

# Passo 2: Calcular quantos dólares é possível comprar com esse valor (dinheiro / 3.27)
print(f'Com R${dinheiro:.2f} é possível comprar US${dinheiro / 3.27:.2f}.')

    # Extra: Calcular quantos euros, yenes e pesos argentinos é possível comprar com esse valor.
    # Considere: €1.00 = R$6.00; ¥1.00 = R$0.04; $1.00 = R$0.01

# Passo 3: Calcular quantos euros é possível comprar com esse valor (dinheiro / 6)
print(f'Com R${dinheiro:.2f} é possível comprar €{dinheiro / 6:.2f}.')

# Passo 4: Calcular quantos yenes é possível comprar com esse valor (dinheiro / 0.04)
print(f'Com R${dinheiro:.2f} é possível comprar ¥{dinheiro / 0.04:.0f}.')

# Passo 5: Calcular quantos pesos argentinos é possível comprar com esse valor (dinheiro / 0.01)
print(f'Com {dinheiro} é possível comprar ${dinheiro / 0.01:.2f}.')
# ----------------------------------------------------------------- Desafio [010]
