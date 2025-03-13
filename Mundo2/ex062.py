# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

from modulo import txt_style as styl, sep


# Passo 1: Solicitar valores para "primeiro termo" e "razão"
print(styl(f"{' FACTORIAL ':=^40}", 'bd', 'p') + "\n")

first_term: int = int(input(styl("First term:", 'n') + " "))
comm_diff: int = int(input(styl("Common difference:", 'n') + " "))
print(styl(sep(first_term * 17), color_ = 'c'))

# Passo 2: Exibir os 10 primeiros termos
current_term: int = first_term
cont: int = 0
while cont != 10:
    print(styl(f"{current_term}", 'bd', 'b'), end = " → ")
    current_term += comm_diff
    cont += 1

print(styl("...", 'bd', 'y'))
print(styl(sep(17), color_ = 'c'))

# Passo 3: Solicitar um valor para "termo final"
# Loop to keep asking the user if they want to show more terms
while True:
    add_terms: int = int(input(styl("How many more terms would you like to see?", 'n') + " "))
    print(styl(sep(17), color_ = 'c'))

    if add_terms == 0:
        break

# Passo 4: Exibir até o o termo final
    while add_terms > 0:
        current_term += comm_diff
        print(styl(f"{current_term}", 'bd', 'b'), end = " → ")
        add_terms -= 1

    print(styl("...", 'bd', 'y'))
    print(styl(sep(17), color_ = 'c'))

print(styl("END", 'bd', 'y'))
# --------------------------| Desafio [062]
