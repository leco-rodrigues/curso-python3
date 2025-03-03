# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

# Passo 1: Receber um valor para "algo"
algo = input('\033[7;40mDigite alguma coisa:\033[m ')

# Passo 2: Exibir o tipo primitivo
print(
      f'\033[1;35mO tipo primitivo de "{algo}" é {type(algo)}.\n'

# Passo 3: Exibir as informações adicionais
      f'É alfabético? {algo.isalpha()}\n' # Verifica se a string contém apenas letras (sem números ou espaços)
      f'É numérico? {algo.isnumeric()}\n' # Verifica se a string contém apenas números inteiros (sem pontos decimais)
      f'É alfanumérico? {algo.isalnum()}\n' # Verifica se a string contém apenas letras e/ou números (sem caracteres especiais ou espaços)
      f'É decimal? {algo.isdecimal()}\n' # Verifica se a string contém apenas números decimais (dígitos 0-9)
      f'É um dígito? {algo.isdigit()}\n' # Verifica se a string contém apenas dígitos (simplesmente números, semelhante a isdecimal)
      f'Tudo está em maiúsculo? {algo.isupper()}\n' # Verifica se todos os caracteres são maiúsculos
      f'Tudo está em minúsculo? {algo.islower()}\n' # Verifica se todos os caracteres são minúsculos
      f'Tem apenas espaços em branco? {algo.isspace()}\n' # Verifica se a string contém apenas espaços em branco (espaços, tubulações, etc.)
      f'Faz parte da tabela ASCII? {algo.isascii()}\n' # Verifica se todos os caracteres pertencem à tabela ASCII (de U+0000 a U+007F)
      f'Pode ser uma palavra reservada? {algo.isidentifier()}\n' # Verifica se a string pode ser usada como nome de variável em Python
      f'Pode ser mostrado na tela? {algo.isprintable()}\n' # Verifica se todos os caracteres podem ser exibidos na tela (sem caracteres de controle, por exemplo)
      f'Todas as palavras estão capitalizadas? {algo.istitle()}\033[m'
      )
# --------------------------------------------------------------------| Desafio [004]
