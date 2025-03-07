# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep


cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m', 'negritociano':'\033[1;36m'}

# Passo 1: Receber valores para "início", "fim" e "passos"
print(f"\t{cores['negritociano']}{' MONTE SUA CONTAGEM ':=^40}{cores['limpa']}")

inicio = int(input(f"{cores['pretoebranco']}Início da contagem:{cores['limpa']} "))
fim = int(input(f"{cores['pretoebranco']}Fim da contagem:{cores['limpa']} "))
passo = int(input(f"{cores['pretoebranco']}Passos entre a contagem:{cores['limpa']} "))
progressiva_regressiva = 1 # Garante que o número final apareça na contagem (progressiva)
mensagem = input(f"{cores['pretoebranco']}Insira a mensagem mostrada ao final da contagem:{cores['limpa']}\n")

if inicio > fim: # Condição para ser considerado uma contagem regressiva
    progressiva_regressiva = -1 # Garante que o número final apareça na contagem (regressiva)
    passo = -abs(passo) # Garante que o número de passos seja negativo

# Passo 2: Exibir a contagem
for contagem in range(inicio, fim + (progressiva_regressiva), passo):
    print(f"{cores['negritoroxo']}{contagem}{cores['limpa']}")
    if contagem != fim:
        sleep(1)

# Passo 3: Exibir a mensagem final
print(f"{cores['negritoroxo']}BOOM!!!! 💀{cores['limpa']}")

if mensagem:
    print(f"{cores['negritoroxo']}{mensagem}{cores['limpa']}")
# -----------------------------------------------------------| Desafio [046]
