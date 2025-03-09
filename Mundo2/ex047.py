# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

cores: dict[str] = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoroxo':'\033[1;35m', 'negritoazul':'\033[1;34m', 'negritovermelho':'\033[1;31m', 'ciano':'\033[36m'}

# Passo 1: Receber valores para dois "números"
print(f"{cores['negritoroxo']}Escolha dois números para exibir todos os pares entre eles:{cores['limpa']}\n")

intervalos: list[int] = []
for i in range(1,3):
    n: int = int(input(f"{cores['pretoebranco']}{i}° número:{cores['limpa']} "))
    intervalos.append(n)

# Passo 2: Exibir os números pares
if min(intervalos) == max(intervalos):
    print(f"\n{cores['negritovermelho']}Os números são iguais, portando não há intervalos para exibir.{cores['limpa']}")

elif min(intervalos) % 2 == 0 and max(intervalos) % 2 == 0 and min(intervalos) + 2 == max(intervalos):
    print(f"{cores['negritovermelho']}Não há números pares entre {min(intervalos)} e {max(intervalos)}, pois eles são consecutivos.{cores['limpa']}")

else:
    inicio: int = min(intervalos) + (1 if min(intervalos) % 2 == 1 else 2)

    print(f"\n{cores['negritoroxo']}Os números pares entre {min(intervalos)} e {max(intervalos)} (excluindo início e fim) são:{cores['limpa']}\n")

    pares: list[str] = []
    for n in range(inicio, max(intervalos), 2):
        print(f"{cores['ciano']}|{cores['limpa']}", end=' ')
        print(f"{cores['negritoazul']}{n}{cores['limpa']}", end=' ')

    print(f"{cores['ciano']}|{cores['limpa']}")
# --------------------------------------------| Desafio [047]
