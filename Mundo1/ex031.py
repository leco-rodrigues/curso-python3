# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km
# e R$0.45 para viagens mais longas.

# Passo 1: Receber um valor para "distância"
distancia = int(input('Qual será a distância, em Km, da viagem? ')) # distância em Km

# Passo 2: Criar uma condição composta que calcule o preço da passagem
if distancia <= 200: # condição de preço R$0.50 por Km (distancia * 0.5)
    print(f'Em uma viagem de {distancia}Km o preço da passagem fica em R${distancia * 0.5:.2f}.')
else:
    print(f'Em uma viagem de {distancia}Km o preço da passgem fica em R${distancia * 0.45:.2f}.') # R$0.45 por Km (distancia * 0.45)
# ----------------------------------------------------------------------------------------- Desafio [031]
