# Crie um programa que leia o nome completo de uma pessoa e mostre:
    # O nome com todas as letras maiúsculas.
    # O nome com todas minúsculas.
    # Quantas letras ao todo (sem considerar espaços).
    # Quantas letras tem o primeiro nome.

# Passo 1: Receber um valor para "nome completo"
nome = input('Digite o seu nome completo: ') # nome completo

# Passo 2: Transformar todas as letras em maiúsculas
print(f'Com letras maiúsculas: {nome.upper()}\n'

# Passo 3: Transformar todas as letras em minúsculas
      f'Com letras minúsculas: {nome.lower()}\n'

# Passo 4: Contar o número total de letras (desconsiderando espaços)
      f'Seu nome completo é composto por {len(nome.replace(' ', ''))} letras.\n'

# Passo 5: Contar o número de letras do primeiro nome
      f'Seu primeiro nome é composto por {len(nome.split()[0])} letras.')
# ----------------------------------------------------------------------- Desafio [022]
