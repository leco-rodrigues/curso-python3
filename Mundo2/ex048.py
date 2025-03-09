# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# Passo 1: Exibir a soma
soma = 0
cont = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        soma += impar
        cont += 1

print(f'\033[1;34mA soma dos {cont} números ímpares, múltiplos de 3, entre 1 e 500 é igual a {soma}.\033[m')
# ----------------------------------------------------------------------------------------------------------| Desafio [048]
