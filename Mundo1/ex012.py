# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Passo 1: Receber um valor para "preço"
p = float(input('Quanto custa esse produto? R$')) # preço

# Passo 2: Calcular com 5% de desconto
print(f'Na promoção de 5% de desconto, de {p:.2f} o preço cai para R${p * 0.95:.2f}!\n' # novo preço = preço * 0.95

    # Extra: Calcular esse valor com 10% de desconto caso seja pago à vista e 8% de aumento caso seja parcelado.
      f'Pagamento à vista tem um desconto de 10%! Cai de R${p:.2f} para apenas R${p * 0.90:.2f}!\n' # à vista = preço * 0.90
      f'Caso opte pelo parcelamento, o preço sobe de R${p:.2f} para R${p * 1.08:.2f}! Um aumento de apenas 8%!') # parcelado = preço * 1.08
# -------------------------------------------------------------------------------------------------------------- Desafio [012]
