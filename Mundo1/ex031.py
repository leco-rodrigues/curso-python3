# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km
# e R$0.45 para viagens mais longas.

# Passo 1: Receber um valor para "distância"
distancia = int(input('\033[7;40mQual será a distância da viagem?\033[m '))

# Passo 2: Exibir o preço da passagem
if distancia <= 200:
    print(f'\033[1;34mEm uma viagem de {distancia} Km, o preço da passagem fica em R${distancia * 0.5:.2f}.\033[m')
else:
    print(f'\033[1;34mEm uma viagem de {distancia} Km, o preço da passagem fica em R${distancia * 0.45:.2f}.\033[1;34m')
# ---------------------------------------------------------------------------------------------------------------------| Desafio [031]
