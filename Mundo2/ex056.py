# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    # A média de idade do grupo.
    # Qual é o nome do homem mais velho
    # Quantas mulheres têm menos de 20 anos.

from typing import Optional


cores: dict[str, str] = {
    'limpa':'\033[m',
    'inverso':'\033[7;40m',
    'negritoroxo':'\033[1;35m',
    'negritoazul':'\033[1;34m',
    'ciano':'\033[36m'
}

def sep(x: Optional[int] = None) -> str:
    if x is None:
        x: int = 22
    return f"{cores['ciano']}-={cores['limpa']}" * x


# Passo 1: Receber quatro valores para "nome", "idade" e "sexo"
nomes: list[str] = []
nomes_masc: list[str] = []
masc_maior_idade: int = 0
nomes_fem: list[str] = []
fem_menor_20: int = 0
idades: list[int] = []
sexos: list[str] = []

print(f"{sep(6)}{cores['negritoroxo']} INSIRA OS DADOS DO GRUPO: {cores['limpa']}{sep(7)}\n")
print(sep())

num_grupo: int = int(input(f"{cores['inverso']}Quantas pessoas há no seu grupo?{cores['limpa']} "))
print(sep())

for p in range(1, num_grupo + 1):
    nome: str = input(f"{cores['inverso']}Nome da {p}° pessoa:{cores['limpa']} ").strip().upper()
    idade: int = int(input(f"{cores['inverso']}Idade da {p}° pessoa:{cores['limpa']} "))
    sexo: str = input(f"{cores['inverso']}Sexo da {p}° pessoa:{cores['limpa']} ").strip().upper()

    sexo = sexo[0]
    print(sep())

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

    if sexo == 'M':
        if idade > masc_maior_idade:
            masc_maior_idade = idade
            nomes_masc = [nome]
        elif idade == masc_maior_idade:
            nomes_masc.append(nome)

    if sexo == 'F':
        if idade < 20:
            fem_menor_20 += 1
            nomes_fem.append(nome)

print(f"\n{sep(11)}{cores['negritoroxo']} DADOS DO GRUPO: {cores['limpa']}{sep(12)}")

for i in range(len(nomes)):
    print(f"{cores['negritoroxo']}Nome: {nomes[i]:20} | Idade: {idades[i]:3} | Sexo: {sexos[i]}{cores['limpa']}")

print(sep(35))

# Passo 2: Exibir a média de idade
print(f"{cores['negritoazul']}A média de idade desse grupo é igual a {sum(idades) / len(idades):.1f}.{cores['limpa']}")

print(sep(35))

# Passo 3: Exibir o nome do homem mais velho
if nomes_masc:
    print(f"{cores['negritoazul']}O(s) homem(ns) mais velho(s) nesse grupo tem {masc_maior_idade} anos.{cores['limpa']}")
    print(f"{cores['negritoroxo']}Nome(s): {', '.join(nomes_masc)}.{cores['limpa']}")
else:
    print(f"{cores['negritoroxo']}Não há homens no grupo.{cores['limpa']}")

print(sep(35))

# Passo 4: Exibir número de mulheres com idade menor que 20
if nomes_fem:
    print(f"{cores['negritoazul']}O número de mulheres com idade menor que 20 nesse grupo é igual a {fem_menor_20}.{cores['limpa']}")
    print(f"{cores['negritoroxo']}Nome(s): {', '.join(nomes_fem)}.{cores['limpa']}")
elif 'F' in sexos:
    print(f"{cores['negritoroxo']}Não há mulheres com menos de 20 anos no grupo.{cores['limpa']}")
else:
    print(f"{cores['negritoroxo']}Não há mulheres no grupo.{cores['limpa']}")

print(sep(35))
# -----------| Desafio [056]
