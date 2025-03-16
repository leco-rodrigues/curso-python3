# Vários números com flag:
    # Crie um programa que leia vários números inteiros pelo teclado.
    # O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
    # No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

from custom_module import txt_style as styl, print_error, sepa_rator as sep_


# Passo 1: Solicitar valores para "número inteiro"
print(styl(f"\t{' COUNT & SUM ':=^40}\n", 'bd'))

total: int = 0
count: int = 0

while True:
    try:
        num: int = int(input(styl("Enter a number (999 to stop):", 'n') + " "))

        if num == 999:
            break

        total += num
        count += 1

    except ValueError:
        print_error("Invalid input. Please enter a valid number.")

sep_(color = 'c')

# Passo 2: Exibir a quantidade
print(styl(f"Total numbers entered: {count}", 'bd', 'p'))
sep_(color = 'c')

# Passo 3: Exibir a soma
print(styl(f"Sum: {total}", 'bd', 'p'))
sep_(color = 'c')

# Passo 4: Exibir mensagem de encerramento
print(styl("Exiting the program... Thank you for using it! 😄", 'bd'))
# --------------------------------------------------------------------| AULA 15 - INTERROMPENDO REPETIÇÕES "WHILE" | DESAFIO [066]
