# Maior e Menor valores:
    # Crie um programa que leia vários números inteiros pelo teclado.
    # No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
    # O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

from custom_module import txt_style as styl, yes_no, print_error, sepa_rator as sep_


# Passo 1: Solicitar valores para "número inteiro"
print(styl(f"\t{' MEAN, BIGGEST & LOWER ':=^40}", 'bd') + "\n")

numbers: list[int] = []
while True:
    try:
        num: int = int(input(styl("Please enter a number:", 'n') + " "))
        numbers.append(num)

        while True:
            add_num: str = str(input(styl("Would you like to enter one more number (y/n)?", 'n') + " ")).strip().lower()
                
            if add_num in ('yes', 'y', 'no', 'n'):
                break
            else:
                print_error()

        if yes_no(add_num):
            continue
        else:
            break

    except ValueError:
        print_error()

print(sep_(15, 'c'))

# Passo 2: Exibir a média
if len(numbers) > 1:
    print(styl(f"The mean between these numbers is {sum(numbers) / len(numbers):,.2f}.", 'bd', 'b'))
    print(sep_(15, 'c'))

# Passo 3: Exibir o maior
    print(styl(f"The biggest number is {max(numbers)}.", 'bd', 'b'))
    print(sep_(15, 'c'))

# Passo 4: Exibir o menor
    print(styl(f"The lowest number is {min(numbers)}.", 'bd', 'b'))
    print(sep_(15, 'c'))

else:
    print(styl(f"The only number is {numbers[0]}.", 'bd', 'p'))
    print(sep_(15, 'c'))

print(styl("Exiting program...", 'bd'))
# ------------------------------------| AULA 14 - ESTRUTURA DE REPETIÇÃO "WHILE" | DESAFIO [065]
