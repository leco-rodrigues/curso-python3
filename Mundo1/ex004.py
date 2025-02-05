# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

# Passo 1: Receber um valor para "algo"
algo = input('Digite qualquer coisa: ')

# Passo 2: Classificar o tipo e obter informações adicionais
print(f'O tipo primitivo de "{algo}" é {type(algo)}.\n' # tipo primitivo
    # Informações adicionais
      f'É alfabético? {algo.isalpha()}\n' # letra alfabética
      f'É numérico? {algo.isnumeric()}\n' # número inteiro
      f'É alfanumérico? {algo.isalnum()}\n' # número e/ou letra alfabética
      f'É decimal? {algo.isdecimal()}\n' # número decimal
      f'É um dígito? {algo.isdigit()}\n' # número...(?)
      f'Tudo está em maiúsculo? {algo.isupper()}\n' # letra maiúscula
      f'Tudo está tudo em minúsculo? {algo.islower()}\n' # letra minúscula
      f'Tem apenas espaços em branco? {algo.isspace()}\n' # espaço em branco (!= espaço vazio)
      f'Faz parte da tabela ASCII? {algo.isascii()}\n' # espaço em branco/vazio ou...(?)
      f'Pode ser uma palavra reservada? {algo.isidentifier()}\n' # possível palavra-chave
      f'Pode ser mostrado na tela? {algo.isprintable()}\n' # "print" é possível
      f'Todas as palavras estão capitalizadas? {algo.istitle()}') # letra maiúscula seguida de minúscula em toda string
# --------------------------------------------------------------- Desafio [004]
