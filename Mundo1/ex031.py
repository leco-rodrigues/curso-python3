# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km
# e R$0.45 para viagens mais longas.

cores= {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}
# Passo 1: Receber um valor para "distância"
distancia = int(input(f'{cores['pretoebranco']}Qual será a distância, em Km, da viagem?{cores['limpa']} ')) # distância em Km

# Passo 2: Criar uma condição composta que calcule o preço da passagem
if distancia <= 200: # condição de preço R$0.50 por Km (distancia * 0.5)
    print(f'{cores['negritoazul']}Em uma viagem de {distancia}Km o preço da passagem fica em R${distancia * 0.5:.2f}{cores['limpa']}.')
else:
    print(f'{cores['negritoazul']}Em uma viagem de {distancia}Km o preço da passgem fica em R${distancia * 0.45:.2f}.{cores['limpa']}') # R$0.45 por Km (distancia * 0.45)
# ------------------------------------------------------------------------------------------------------------------------------------| Desafio [031]
