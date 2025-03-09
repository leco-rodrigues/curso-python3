# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# Passo 1: Receber um valor para "número"
n: int = int(input(f'\033[7;40mEscolha um número para fazer a tabuada:\033[m '))

# Passo 2: Exibir a tabuada (usando for)
print(f'\033[1;35mTabuada do {n}:\033[m\n')
for num in range(1, 11):
    print(f'\033[1;34m{n} x {num:2} = {n * (num)}\033[m')
# ------------------------------------------------------| Desafio [049]
