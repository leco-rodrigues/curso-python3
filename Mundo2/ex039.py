# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    # Se ele ainda vai se alistar ao exército militar
    # Se é a hora de se alistar
    # Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date


cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m', 'negritoroxo':'\033[1;35m'}

# Passo 1: Receber um valor para "ano de nascimento"
ano_nascimento = int(input(f"{cores['pretoebranco']}Em que ano você nasceu?{cores['limpa']} "))
sexo = input(f"{cores['pretoebranco']}Qual o seu sexo?{cores['limpa']} ")

# Passo 2: Exibir o status de alistamento e o tempo restante/de atraso
if sexo == 'masculino':
    idade = date.today().year - ano_nascimento
    ano_alistamento = ano_nascimento + 18
    
    if idade == 18:
        print(f"{cores['negritoazul']}Você está com {idade} anos, já é hora de se alistar.{cores['limpa']}")
    elif idade < 18:
        tempo_restante = 18 - idade

        print(f"{cores['negritoazul']}Você está com {idade} anos, deverá se alistar daqui a {tempo_restante} anos, em {ano_alistamento}.{cores['limpa']}")
    else:
        tempo_perdido = idade - 18
        print(f"{cores['negritoazul']}Você está com {idade} anos, o prazo para o alistamento já passou há {tempo_perdido} anos, em {ano_alistamento}.{cores['limpa']}")

else:
    print(f"{cores['negritoroxo']}Você não precisa realizar o alistamento militar obrigatório.{cores['limpa']}")
# -------------------------------------------------------------------------------------------------------------| Desafio [039]
