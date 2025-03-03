# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere: US$1.00 = R$3.27

# Passo 1: Receber um valor para "dinheiro"
dinheiro = float(input('\033[7;40mQuantos reais você tem na carteira?\033[m R$'))

# Passo 2: Exibir quantos dólares é possível comprar
print(
      f'\033[1;34mCom R${dinheiro:.2f} é possível comprar US${dinheiro / 3.27:.2f}.\n'

    # Extra: Euros, yenes e pesos argentinos
    # Considere: €1.00 = R$6.00; ¥1.00 = R$0.04; $1.00 = R$0.01
      f'Com R${dinheiro:.2f} é possível comprar €{dinheiro / 6:.2f}.\n'
      f'Com R${dinheiro:.2f} é possível comprar ¥{dinheiro / 0.04:.0f}.\n'
      f'Com R${dinheiro:.2f} é possível comprar ${dinheiro / 0.01:.2f}.\033[m'
      )
# ----------------------------------------------------------------------------| Desafio [010]
