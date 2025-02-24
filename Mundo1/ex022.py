# Crie um programa que leia o nome completo de uma pessoa e mostre:
    # O nome com todas as letras maiúsculas.
    # O nome com todas minúsculas.
    # Quantas letras ao todo (sem considerar espaços).
    # Quantas letras tem o primeiro nome.

# Passo 1: Receber um valor para "nome"
nome = input('\033[7;40mDigite o seu nome completo:\033[m ') # nome completo

# Passo 2: Transformar e exibir todas as letras em maiúsculas e em minúsculas
print(f'\033[1;35mCom letras maiúsculas: {nome.upper()}\n' # maiúsculas
      f'Com letras minúsculas: {nome.lower()}\033[m\n' # minúsculas

# Passo 3: Contar e exibir o número de letras do peimeiro nome e o número total de letras (desconsiderando espaços)
      f'\033[1;34mSeu nome completo é composto por {len(nome.replace(' ', ''))} letras.\n' # número total
      f'Seu primeiro nome é composto por {len(nome.split()[0])} letras.\033[m') # número do primeiro nome
# ----------------------------------------------------------------------------| Desafio [022]
