# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# Passo 1: Receber valores para "valor da casa", "salário" e "quantos anos até pagar"
valor_casa = float(input('Qual o valor da casa? R$')) #  valor do empréstimo
salario = float(input('Qual o seu salário? R$'))
anos_pagando = int(input('Em quantos anos irá pagar o empréstimo? ')) # em quantos anos será pago
print(f'O valor do empréstimo seria de R${valor_casa:.2f}. Seu salário é de R${salario:.2f}, e você pagará em {anos_pagando} anos?')

# Passo 2: Criar uma condição composta para calcular o valor da prestação mensal (acima de 30% do salário, será negado)
prestação_mensal = valor_casa / (anos_pagando * 12) # prestação = valor da casa / (anos pagando * 12 (meses por ano))
if prestação_mensal <= salario * 0.30: # condição para aprovação do empréstimo
    print(f'Empréstimo APROVADO! As mensalidades ficarão em R${prestação_mensal:.2f}.')
else:
    print(f'Empréstimo NEGADO! Nessas condições, as mensalidades ficariam em R${prestação_mensal:.2f}, excedendo 30% do seu salário atual.')
# -----------------------------------------------------------------------------------------------------------------------------------------| Desafio [036]
