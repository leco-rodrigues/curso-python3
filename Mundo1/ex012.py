# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Passo 1: Receber um valor para "preço"
preco = float(input('\033[7;40mQuanto custa esse produto?\033[m R$'))

# Passo 2: Exibir com o desconto
print(
      f'\033[1;34mNa promoção de 5%, de {preco:.2f}, o preço cai para R${preco * 0.95:.2f}!\n'

    # Extra: Com 10% de desconto caso seja pago à vista e 8% de aumento caso seja parcelado
      f'No pagamento à vista tem um desconto de 10%! O preço cai, de R${preco:.2f}, para apenas R${preco * 0.90:.2f}!\n'
      f'Caso opte pelo parcelamento, o preço sobe, de R${preco:.2f}, para R${preco * 1.08:.2f}! Um aumento de apenas 8%!\033[m'
      )
# -----------------------------------------------------------------------------------------------------------------------------| Desafio [012]
