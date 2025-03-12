# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

from modulo import txt_style as styl, sep


# Passo 1: Solicitar valores para "primeiro termo" e "razão"
term_x: int = int(input(styl("First term:", 'n') + " "))
comm_diff: int = int(input(styl("Common difference:", 'n') + " "))

# Passo 2: Exibir os 10 primeiros termos
terms: list[int] = [term_x]
cont: int = 0
while cont != 9:
    term_n: int = term_x + comm_diff
    terms.append(term_n)
    term_x = term_n
    cont += 1

print(styl(sep(23), color_ = 'c'))
print(styl("The 10 first terms of that AP are: " + ", ".join(map(str, terms)) + ".", 'bd', 'b'))
# ---------------------------------------------------------------------------------------------| Desafio [061]
