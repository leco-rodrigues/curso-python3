# Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou ÍMPAR.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m'}
# Passo 1: Receber um valor para "número"
n = int(input(f'{cores['pretoebranco']}Digite um número inteiro:{cores['limpa']} ')) # número inteiro

# Passo 2: Criar uma condição composta para dizer se é "par" ou "ímpar"
if n % 2 == 0:
    print(f'{cores['negritoroxo']}{n} é PAR!{cores['limpa']}')
else:
    print(f'{cores['negritoroxo']}{n} é ÍMPAR!{cores['limpa']}')
# -------------------------------------------------------------| Desafio [030]
