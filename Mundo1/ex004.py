# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# Passo 1: Receber um valor qualquer
algo = input('Digite alguma coisa: ')

# Classificar o tipo desse valor e obter as demais informações
print(f'O tipo primitivo de {algo} é {type(algo)}.')
    # Informações adicionais
print(f'É alfabético? {algo.isalpha()}') # letra(s) alfabética(s)
print(f'É numérico? {algo.isnumeric()}') # número(s) inteiro(s)
print(f'É alfanumérico? {algo.isalnum()}') # número(s) e/ou letra(s) alfabética(s)
print(f'É decimal? {algo.isdecimal()}') # número(s) decimal(s)
print(f'É um dígito? {algo.isdigit()}') # número...(?)
print(f'Tudo está em maiúsculo? {algo.isupper()}')
print(f'Tudo está tudo em minúsculo? {algo.islower()}')
print(f'Tem apenas espaços? {algo.isspace()}') # espaço(s) em branco (!= espaço vazio)
print(f'Faz parte da tabela ASCII? {algo.isascii()}') # espaço(s) em branco/vazio ou
print(f'Pode ser uma palavra reservada? {algo.isidentifier()}')
print(f'Pode ser mostrado na tela? {algo.isprintable()}') # "print" é possível
print(f'Está capitalizada? {algo.istitle()}') # letra maiúscula seguida de minúscula
# --------------------------------------------------- Desafio [004]
