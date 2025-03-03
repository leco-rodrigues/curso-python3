# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite.

# Passo 1: Receber um valor para "velocidade"
velocidade = int(input('\033[7;40mA qual velocidade você estava dirigindo?\033[m '))

# Passo 2: Exibir o valor da multa
if velocidade > 80:
    print(f'\033[1;34m{velocidade}Km?! A sua multa será de R${(velocidade - 80) * 7:.2f}!\033[m')
print('\033[1;35mEstá liberado, tenha um bom dia! E dirija com cuidado!\033[m')
# ----------------------------------------------------------------------------| Desafio [029]
