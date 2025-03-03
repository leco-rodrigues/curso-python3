# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

# Passo 1: Receber um valor para "temperatura"
temperatura = float(input('\033[7;40mQual a temperatura local em Celsius?\033[m '))

# Passo 2: Exibir em Fahrenheit
print(f'\033[1;34mUma temperatura de {temperatura:.1f} °C, convertida em Fahrenheit, corresponde a {(temperatura * 1.8) + 32:.1f} °F.\033[m')
# ----------------------------------------------------------------------------------------------------------------------------------------| Desafio [014]
