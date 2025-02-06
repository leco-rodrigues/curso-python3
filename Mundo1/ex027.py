# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
    # Ex: Ana Maria de Souza
    #     primeiro - Ana
    #     último = Souza

# Passo 1: Receber um valor para "nome completo"
nome = input('Digite seu nome completo: ').strip() # nome completo

# Passo 2: Exibir o primeiro e o último nome
print(f'O seu primeiro nome é: {nome.split()[0]}\n' # primeiro nome
      f'E o seu último nome é: {nome.split()[-1]}') # último nome
# ------------------------------------------------- Desafio [027]
