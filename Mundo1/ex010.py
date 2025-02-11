# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere: US$1.00 = R$3.27

# Passo 1: Receber um valor para "dinheiro"
d = float(input(f'\033[7;40mQuantos reais você tem na carteira?\033[m R$')) # dinheiro

# Passo 2: Calcular e exibir quantos dólares é possível comprar
print(f'\033[1;34mCom R${d:.2f} é possível comprar US${d / 3.27:.2f}.\n' # dólares = dinheiro / 3.27

    # Extra: Euros, yenes e pesos argentinos
    # Considere: €1.00 = R$6.00; ¥1.00 = R$0.04; $1.00 = R$0.01
      f'Com R${d:.2f} é possível comprar €{d / 6:.2f}.\n' # euro = dinheiro / 6
      f'Com R${d:.2f} é possível comprar ¥{d / 0.04:.0f}.\n' # yene = dinheiro / 0.04
      f'Com R${d:.2f} é possível comprar ${d / 0.01:.2f}.\033[m') # peso argentino / 0.01
# --------------------------------------------------------------| Desafio [010]
