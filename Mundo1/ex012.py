# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Passo 1: Receber o valor de "preço"
preço = float(input('Quanto custa esse produto? R$'))

# Preço 2: Calcular esse valor com 5% de desconto (preço * 0.95)
print(f'Na promoção de 5% de desconto, de {preço:.2f} o preço cai para R${preço * 0.95:.2f}!')

    # Extra: Calcular esse valor com 10% de desconto caso seja pago à vista, e 8% de aumento caso seja à prazo.

# Passo 3: Calcular esse valor com 10% de desconto (preço * 0.90)
print(f'Pagamento à vista tem um desconto de 10%! De R${preço:.2f}, por apenas R${preço * 0.90:.2f}!')

# Passo 4: Calcular esse valor com 8% de aumento (preço * 1.08)
print(f'Caso opte pelo parcelamento, o preço de R${preço:.2f} sobe para R${preço * 1.08:.2f}! Um aumento de apenas 8%!')
# ---------------------------------------------------------------------------------------------------------------------- Desafio [012]
