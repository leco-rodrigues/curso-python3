# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
    # Ex: Ana Maria de Souza
    #     primeiro - Ana
    #     último = Souza

# Passo 1: Receber um valor para "nome"
nome = input('\033[7;40mDigite seu nome completo:\033[m ').strip() # nome completo

# Passo 2: Exibir o primeiro e o último nome
print(f'\033[1;35mO seu primeiro nome é {nome.split()[0]}\n' # primeiro nome
      f'E o seu último nome é {nome.split()[-1]}\033[m') # último nome
# -----------------------------------------------------| Desafio [027]
