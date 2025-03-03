# Crie um programa que leia o nome completo de uma pessoa e mostre:
    # O nome com todas as letras maiúsculas.
    # O nome com todas minúsculas.
    # Quantas letras ao todo (sem considerar espaços).
    # Quantas letras tem o primeiro nome.

# Passo 1: Receber um valor para "nome"
nome = input('\033[7;40mDigite o seu nome completo:\033[m ')
print(
      f'\033[1;35mSeu nome completo é {nome}.\n'

# Passo 2: Exibir em letras maiúsculas
      f'Em letras maiúsculas: {nome.upper()}\n'
      
# Passo 3: Exibir em letras minúsculas      
      f'Em letras minúsculas: {nome.lower()}\033[m\n'

# Passo 4: Exibir o número total de letras
      f'\033[1;34mSeu nome completo é composto por {len(nome.replace(' ', ''))} letras.\n'
      
# Passo 5: Exibir o número de letras do primeiro nome      
      f'Seu primeiro nome é composto por {len(nome.split()[0])} letras.\033[m'
      )
# ----------------------------------------------------------------------------| Desafio [022]
