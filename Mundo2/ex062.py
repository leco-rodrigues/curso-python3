# Super Progressão Aritmética v3.0:
    # Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
    # O programa encerra quando ele disser que quer mostrar 0 termos.

from custom_module import txt_style as styl, error_message as err_msg, sepa_rator as sep_


def print_error() -> None:
    """Print a formatted error message."""
    print(sep_(22, 'c'))
    print(err_msg())
    print(sep_(22, 'c'))


# Passo 1: Solicitar valores para "primeiro termo" e "razão"
print(styl(f"\t{' ARITHMETIC PROGRESSION ':=^40}", 'bd') + "\n")

while True:
    try:
        first_term: int = int(input(styl("First term:", 'n') + " "))
        
        while True:
            try:
                comm_diff: int = int(input(styl("Common difference:", 'n') + " "))
                break
            except ValueError:
                print_error()
        break

    except ValueError:
        print_error()

print(sep_(22, 'c'))

# Passo 2: Exibir os 10 primeiros termos
print(styl("The first 10 terms of that AP are: ", 'bd', 'p'))

current_term: int = first_term
count: int = 0
while count < 10:
    print(styl(f"{current_term:,}", 'bd', 'b'), end = " → ")
    current_term += comm_diff
    count += 1

print(styl("...", 'bd', 'g'))
print(sep_(22, 'c'))

# Passo 3: Solicitar um valor para "termo final"
while True:
    try:
        add_terms: int = int(input(styl("How many more terms would you like to see?", 'n') + " "))
        print(sep_(22, 'c'))

        if add_terms <= 0:
            break

    except ValueError:
        print_error()
        continue

# Passo 4: Exibir até o termo final
    print(styl(f"The next {add_terms:,} term{'s' if add_terms > 1 else ''} {'are' if add_terms > 1 else 'is'}:", 'bd', 'p'))

    count += add_terms
    while add_terms > 0:
        print(styl(f"{current_term:,}", 'bd', 'b'), end = " → ")
        current_term += comm_diff
        add_terms -= 1

    print(styl("...", 'bd', 'g'))
    print(sep_(22, 'c'))

print(styl(f"Progression finalized with {count:,} terms shown.", 'bd', 'p'))

print(sep_(22, 'c'))
print(styl("Exiting program...", 'bd'))
# ------------------------------------| AULA 14 - ESTRUTURA DE REPETIÇÃO "WHILE" | DESAFIO [062]
