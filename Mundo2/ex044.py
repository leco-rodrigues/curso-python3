# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
    # À vista dinheiro/cheque: 10% de desconto
    # À vista no cartão: 5% de desconto
    # Em até 2x no cartão: preço normal
    # 3x ou mais no cartão: 20% de juros

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m', 'negritoazul':'\033[1;34m', 'negritociano':'\033[1;36m'}

# Passo 1: Receber valores para "preço" e "condição de pagamento"
print(f"\t{cores['negritociano']}{' LOJA PREÇO BAIXO ':=^40}{cores['limpa']}")

preco = float(input(f"{cores['pretoebranco']}Valor da compra:{cores['limpa']} R$"))
print(f"""{cores['negritoroxo']}
\tFORMAS DE PAGAMENTO:
[1] À vista em dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de juros{cores['limpa']}\n"""
)
condicao_pagamento = int(input(f"{cores['pretoebranco']}Forma de pagamento:{cores['limpa']} "))

# Passo 2: Exibir o valor a ser pago
if condicao_pagamento == 1:
    print(f"{cores['negritoazul']}O preço do produto ficará em R${preco * 0.90:.2f}.{cores['limpa']}")
elif condicao_pagamento == 2:
    print(f"{cores['negritoazul']}O preço do produto ficará em R${preco * 0.95:.2f}.{cores['limpa']}")
elif condicao_pagamento == 3:
    print(f"{cores['negritoroxo']}O preço do produto ficará em R${preco:.2f}, parcelado em 2 vezes de R${preco / 2:.2f} sem juros.{cores['limpa']}")
elif condicao_pagamento == 4:
    parcelas = int(input(f"{cores['pretoebranco']}Número de parcelas:{cores['limpa']} "))
    print(f"{cores['negritoazul']}O preço do produto ficará em R${preco * 1.20:.2f}, parcelado em {parcelas} vezes de R${preco * 1.20 / parcelas:.2f}.{cores['limpa']}")
else:
    print(f"{cores['negritoroxo']}Opção INVÁLIDA! Por favor, tente novamente.{cores['limpa']}")
# --------------------------------------------------------------------------------------------| Desafio [044]
