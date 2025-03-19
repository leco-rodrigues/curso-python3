# Simulador de Caixa Eletrônico:
    # Crie um programa que simule o funcionamento de um caixa eletrônico.
    # No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
    # OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

from custom_module import txt_style as styl, print_error, sepa_rator as sep_


# Passo 1: Solicitar um valor para "saque"
print(styl(f"\t{' ATM ':=^40}\n", 'bd'))

while True:
    try:
        withdraw: int = int(input(styl("How much do you want to withdraw:", 'n') + " R$"))
        if withdraw > 0:
            break
        else:
            print_error("Invalid input. Please enter a positive integer.")
    except ValueError:
        print_error("Invalid input. Please enter an integer.")

sep_(color = 'c')

# Passo 2: Exibir cédulas entregues
bills_50 = withdraw // 50
withdraw %= 50

bills_20 = withdraw // 20
withdraw %= 20

bills_10 = withdraw // 10
withdraw %= 10

bills_1 = withdraw

print(styl("Bills distribution:", 'bd', 'p'))

if bills_50:
    print(styl(f"R$50 bills = {bills_50}", 'bd', 'p'))
if bills_20:
    print(styl(f"R$20 bills = {bills_20}", 'bd', 'p'))
if bills_10:
    print(styl(f"R$10 bills = {bills_10}", 'bd', 'p'))
if bills_1:
    print(styl(f"R$1 bills = {bills_1}", 'bd', 'p'))

sep_(color = 'c')

# Passo 3: Exibir mensagem de encerramento
print(styl("Exiting the program... Thank you for using it! 😄"))
# --------------------------------------------------------------| AULA 15 - INTERROMPENDO REPETIÇÕES "WHILE" | DESAFIO [071]
