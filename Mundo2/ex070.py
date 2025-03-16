# Estatísticas em produtos:
    # Crie um programa que leia o nome e o preço de vários produtos.
    # O programa deverá perguntar se o usuário vai continuar.
    # No final, mostre
        # A) Qual é o total gasto na compra.
        # B) Quantos produtos custam mais de R$1000.
        # C) Qual é o nome do produto mais barato.

from custom_module import txt_style as styl, print_error, sepa_rator as sep_


# Passo 1: Solicitar valores para "nome" e "preço"
print(styl(f"\t{' NAME & PRICE ':=^40}\n"))

total: float = 0
above_1000: int = 0
cheaper_name: str = "N/A"
cheaper_price: float = float("inf")

while True:
    while True:
        product: str = str(input(styl("Product's name:", 'n') + " ")).strip().title()

        if product:
            break
        else:
            print_error("Invalid input. Please don't use special characters nor leave an empty space.")

    while True:
        try:
            price: float = float(input(styl("Product's price: R$", 'n') + ""))
            
            if price > 0:
                break
            else:
                print_error("Invalid input. Please enter a price above 0.")

        except ValueError:
            print_error("Invalid input. Please enter an valid price.")

    total += price
    
    if price > 1000:
        above_1000 += 1

    if price < cheaper_price:
        cheaper_price = price
        cheaper_name = product

    while True:
            choice: str = str(input(styl("Do you want to add more products (Y/N)?", 'n') + " ")).strip().lower()

            if choice in ('yes', 'y', 'no', 'n'):
                break
            else:
                print_error("Invalid input. Please enter 'yes'/'y' or 'no'/'n'.")

    if choice in ('no', 'n'):
        break

sep_(color = 'c')

# Passo 2: Exibir o total gasto
print(styl(f"Total spent: R${total:,.2f}", 'bd', 'p'))
sep_(color = 'c')

# Passo 3: Exibir quantos custam mais de R$1000,00
print(styl(f"Number of products above R$1000.00: {above_1000:,}", 'bd', 'p'))
sep_(color = 'c')

# Passo 4: Exibir o nome do mais barato
print(styl(f"Cheapest product: {cheaper_name} (R${cheaper_price:,.2f})", 'bd', 'p'))
sep_(color = 'c')

# Passo 5: Exibir mensagem de encerramento
print(styl("Exiting program... Thank you for using it! 😄", 'bd'))
# ----------------------------------------------------------------| AULA 15 - INTERROMPENDO REPETIÇÕES "WHILE" | DESAFIO [070]
