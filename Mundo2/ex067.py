# Tabuada v3.0:
    # Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
    # O programa será interrompido quando o número solicitado for negativo.

from custom_module import txt_style as styl, print_error, sepa_rator as sep_


# Passo 1: Solicitar valores para "número inteiro"
print(styl(f"\t{' MULTIPLICATION TABLE ':=^40}\n", 'bd'))

while True:
    try:
        num: int = int(input(styl("Please enter a number (negative number to stop):", 'n') + " "))

        if num < 0:
            break

# Passo 2: Exibir a tabuada
        sep_(color = 'c')
        print(styl(f"Here are the multiplication table for {num}:\n", 'bd', 'p'))

        for i in range(1, 11):
            print(styl(f"{num} x {i:2} = {num * i}", 'bd', 'p'))

        sep_(color = 'c')

    except ValueError:
        print_error("Invalid input. Please enter a valid number.")

# Passo 3: Exibir mensagem de encerramento
sep_(color = 'c')
print(styl("Exiting the program... Thank you for using it! 😄", 'bd'))
# --------------------------------------------------------------------| AULA 15 - INTERROMPENDO REPETIÇÕES "WHILE" | DESAFIO [067]
