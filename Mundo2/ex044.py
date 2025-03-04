# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
    # À vista dinheiro/cheque: 10% de desconto
    # À vista no cartão: 5% de desconto
    # Em até 2x no cartão: preço normal
    # 3x ou mais no cartão: 20% de juros

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m', 'negritoazul':'\033[1;34m'}

# Passo 1: Receber valores para "preço" e "condição de pagamento"
preco = float(input(f"{cores['pretoebranco']}Digite o preço do pruduto:{cores['limpa']} R$"))
condição_pagamento = int(input(f"{cores['pretoebranco']}Para pagamento à vista em dinheiro, cheque ou cartão, digite 1. Para parcelamento no cartão, digite 2:{cores['limpa']} "))

# Passo 2: Exibir o valor a ser pago
if condição_pagamento == 1:
    a_vista = int(input(f"{cores['pretoebranco']}Para pagamento em dinheiro ou cheque, digite 1. Para pagamento no cartão, digite 2:{cores['limpa']} "))
    
    if a_vista == 1:
        print(f"{cores['negritoazul']}O preço do produto sairá com 10% de desconto, de R${preco} por R${preco * 0.90}.{cores['limpa']}")
    else:
        print(f"{cores['negritoazul']}O preço do produto sairá com 5% de desconto, de R${preco} por R${preco * 0.95}.{cores['limpa']}")

else:
    parcelado = int(input(f"{cores['pretoebranco']}Para parcelamento em 2x, digite 1. Para parcelamento em 3x ou mais, digite 2:{cores['limpa']} "))

    if parcelado == 1:
        print(f"{cores['negritoroxo']}O produto sairá com o preço normal, R${preco}.{cores['limpa']}")
    else:
        print(f"{cores['negritoazul']}O preço do produto sairá com 20% de juros, de R${preco} por R${preco * 1.20}.{cores['limpa']}")
# ----------------------------------------------------------------------------------------------------------------------------------| Desafio [044]
