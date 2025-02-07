# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite.

# Passo 1: Receber um valor para "velocidade"
v = int(input('A qual velocidade você estava dirigindo? ')) # velocidade em Km

# Passo 2: Criar uma condição simples para dizer se haverá multa
if v > 80: # condição para multa
    print(f'{v}Km?! Sua multa será de R${(v - 80) * 7:.2f}!') # cálculo da multa ((v - 80) * 7)
print('Agora pode ir.')
# --------------------- Desafio [029]
