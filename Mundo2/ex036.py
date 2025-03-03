# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m', 'negritoazul':'\033[1;34m'}

# Passo 1: Receber valores para "empréstimo", "salário" e "anos pagando"
emprestimo = float(input(f"{cores['pretoebranco']}Qual o valor da casa?{cores['limpa']} R$"))
salario = float(input(f"{cores['pretoebranco']}Qual o seu salário?{cores['limpa']} R$"))
anos_pagando = int(input(f"{cores['pretoebranco']}Em quantos anos irá pagar o empréstimo?{cores['limpa']} "))
print(f"{cores['negritoroxo']}O valor do empréstimo seria de R${emprestimo:.2f}. Seu salário é de R${salario:.2f}, e você pagará em {anos_pagando} anos?{cores['limpa']}")

# Passo 2: Exibir se o empréstimo foi aprovado
prestação_mensal = emprestimo / (anos_pagando * 12)
if prestação_mensal <= salario * 0.30:
    print(f"{cores['negritoazul']}Empréstimo APROVADO! As mensalidades ficarão em R${prestação_mensal:.2f}, por {anos_pagando} anos.{cores['limpa']}")
else:
    print(f"{cores['negritoazul']}Empréstimo NEGADO! Nessas condições, as mensalidades ficariam em R${prestação_mensal:.2f}, excedendo 30% do seu salário atual.{cores['limpa']}")
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| Desafio [036]
