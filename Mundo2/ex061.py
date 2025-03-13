# Progressão Aritmética v2.0:
    # Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

from custom_module import txt_style as styl, error_message as err_msg, sepa_rator as sep_


# Passo 1: Solicitar valores para "primeiro termo" e "razão"
print(styl(f"\t{' ARITHMETIC PROGRESSION ':=^40}\n"))

while True:
    try:
        term_x: int = int(input(styl("First term:", 'n') + " "))
        
        while term_x:
            try:
                comm_diff: int = int(input(styl("Common difference:", 'n') + " "))
                break
            except ValueError:
                print(err_msg())
        break

    except ValueError:
        print(err_msg())

# Passo 2: Exibir os 10 primeiros termos
terms: list[int] = [term_x]
cont: int = 1
while cont != 10:
    term_n: int = term_x + comm_diff
    terms.append(term_n)
    term_x = term_n
    cont += 1

print(styl(sep_(26, 'c')))
print(styl("The first 10 terms of that AP are: " + ", ".join(map(str, terms)) + ".", 'bd', 'b'))

print(sep_(26, 'c'))
print(styl("Exiting program...", 'bd'))
# ------------------------------------| AULA 14 - ESTRUTURA DE REPETIÇÃO "WHILE" | DESAFIO [061]
