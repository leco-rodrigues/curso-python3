# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere: US$1.00 = R$3.27

# Passo 1: Receber um valor para "dinheiro"
d = float(input('Quantos reais você tem na carteira? R$')) # dinheiro

# Passo 2: Calcular quantos dólares é possível comprar
print(f'Com R${dinheiro:.2f} é possível comprar US${d / 3.27:.2f}.\n' # dólares = dinheiro / 3.27

    # Extra: Calcular quantos euros, yenes e pesos argentinos é possível comprar.
    # Considere: €1.00 = R$6.00; ¥1.00 = R$0.04; $1.00 = R$0.01
      f'Com R${d:.2f} é possível comprar €{d / 6:.2f}.\n' # euro = dinheiro / 6
      f'Com R${d:.2f} é possível comprar ¥{d / 0.04:.0f}.\n' # yene = dinheiro / 0.04
      f'Com R${d:.2f} é possível comprar ${d / 0.01:.2f}.') # peso argentino / 0.01
# --------------------------------------------------------- Desafio [010]
