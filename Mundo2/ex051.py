# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m', 'negritoazul':'\33[1;34m'}

# Passo 1: Receber valores para "termo" e "razão"
termo_um = int(input(f"{cores['pretoebranco']}Digite o primeiro termo da PA:{cores['limpa']} "))
razao = int(input(f"{cores['pretoebranco']}Digite a razão da PA:{cores['limpa']} "))
termo_final = termo_um + (razao * 10)

# Passo 2: Exibir os 10 primeiros termos
print(f"{cores['negritoroxo']}Os 10 primeiros termos dessa PA são:{cores['limpa']}\n")
for t in range(termo_um, termo_final, razao):
    print(f"{cores['negritoazul']}{t}{cores['limpa']}")
# ----------------------------------------------------| Desafio [051]
