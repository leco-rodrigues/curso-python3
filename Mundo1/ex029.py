# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite.

# Passo 1: Receber um valor para "velocidade"
v = int(input('\033[7;40mA qual velocidade você estava dirigindo?\033[m ')) # velocidade em Km

# Passo 2: Criar uma condição simples para dizer se haverá multa
if v > 80: # condição para multa
    print(f'\033[1;34m{v}Km?! Você será multado em R${(v - 80) * 7:.2f}!\033[m') # cálculo da multa ((v - 80) * 7)
print('\033[1;35mJá pode ir! Tenha um bom dia!\033[m')
# ---------------------------------------------------| Desafio [029]
