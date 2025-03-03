# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    # Se ele ainda vai se alistar ao exército militar
    # Se é a hora de se alistar
    # Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}

# Passo 1: Receber um valor para "ano de nascimento"
ano_nascimento = int(input(f"{cores['pretoebranco']}Em que ano você nasceu?{cores['limpa']} "))

# Passo 2: Exibir o status de alistamento e o tempo restante/de atraso
idade = 2025 - ano_nascimento
if idade == 18:
    print(f"{cores['negritoazul']}Você está com {idade} anos, já é hora de se alistar.{cores['limpa']}")
elif idade < 18:
    tempo_restante = 18 - idade
    print(f"{cores['negritoazul']}Você está com {idade} anos, deverá se alistar daqui a {tempo_restante} anos.{cores['limpa']}")
else:
    tempo_perdido = idade - 18
    print(f"{cores['negritoazul']}Você está com {idade} anos, o prazo para o alistamento já passou há {tempo_perdido} anos.{cores['limpa']}")
# ------------------------------------------------------------------------------------------------------------------------------------------| Desafio [039]
