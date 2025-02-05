# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

# Passo 1: Receber um valor qualquer
algo = input('Digite alguma coisa: ')

# Passo 2: Classificar o tipo desse valor
print(f'O tipo primitivo de {algo} é {type(algo)}.')

# Passo 3: Obter as informações adicionais desse valor
print(f'É alfabético? {algo.isalpha()}') # letra alfabética
print(f'É numérico? {algo.isnumeric()}') # número inteiro
print(f'É alfanumérico? {algo.isalnum()}') # número e/ou letra alfabética
print(f'É decimal? {algo.isdecimal()}') # número decimal
print(f'É um dígito? {algo.isdigit()}') # número...(?)
print(f'Tudo está em maiúsculo? {algo.isupper()}') # autoexplicativo
print(f'Tudo está tudo em minúsculo? {algo.islower()}') # autoexplicativo
print(f'Tem apenas espaços? {algo.isspace()}') # espaço(s) em branco (!= espaço vazio)
print(f'Faz parte da tabela ASCII? {algo.isascii()}') # espaço(s) em branco/vazio ou...(?)
print(f'Pode ser uma palavra reservada? {algo.isidentifier()}')
print(f'Pode ser mostrado na tela? {algo.isprintable()}') # "print" é possível
print(f'Está capitalizada? {algo.istitle()}') # letra maiúscula seguida de minúscula
# ------------------------------------------- Desafio [004]
