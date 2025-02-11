# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

# Passo 1: Receber um valor para "temperatura"
c = float(input('\033[7;40mDigite a temperatura em °C:\033[m ')) # Celsius

# Passo 2: Converter e exibir em "Fahrenheit"
print(f'\033[1;34mA temperatura de {c:.1f}°C, convertida em Fahrenheit, corresponde a {(c * 1.8) + 32:.1f}°F.\033[m') # Fahrenheit = Celsius * 1.8 + 32
# ------------------------------------------------------------------------------------------------------------------| Desafio [014]
