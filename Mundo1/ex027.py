# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
    # Ex: Ana Maria de Souza
    #     primeiro - Ana
    #     último = Souza

# Passo 1: Receber um valor para "nome"
nome = input('\033[7;40mDigite seu nome completo:\033[m ').strip()
print(f'\033[1;35mSeu nome completo é: {nome}\n'

# Passo 2: Exibir o primeiro nome
      f'Seu primeiro nome é: {nome.split()[0]}\n'

# Passo 3: Exibir o último nome
      f'Seu último nome é: {nome.split()[-1]}\033[m'
      )
# --------------------------------------------------| Desafio [027]
