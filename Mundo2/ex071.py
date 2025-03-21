# Simulador de Caixa Eletrônico:
    # Crie um programa que simule o funcionamento de um caixa eletrônico.
    # No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
    # OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

from custom_module import txt_style as styl, print_error, sepa_rator as sep_


# Passo 1: Solicitar um valor para "saque"
print(styl(f"\t{' ATM ':=^40}\n", 'bd'))

while True:
    try:
        withdraw: int = int(input(styl("How much do you want to withdraw?", 'n') + " R$"))
        if withdraw > 0:
            break
        else:
            print_error("Invalid input. Please enter a positive integer.")
    except ValueError:
        print_error("Invalid input. Please enter an integer.")

sep_(color = 'c')

# Passo 2: Exibir cédulas entregues
bills_available: list[int] = [50, 20, 10, 1]
bills_distribution: dict[int, int] = {}

for bill in bills_available:
    bills_distribution[bill], withdraw = divmod(withdraw, bill)

print(styl("Bills Distribution:\n", 'bd', 'p'))

for bill, count in bills_distribution.items():
    if count:
        print(styl(f"R${bill:<2} bills: {count:2}", 'bd', 'p'))

sep_(color = 'c')

# Passo 3: Exibir mensagem de encerramento
print(styl("Exiting the program... Thank you for using it! 😄", 'bd'))
# --------------------------------------------------------------------| AULA 15 - INTERROMPENDO REPETIÇÕES "WHILE" | DESAFIO [071]
