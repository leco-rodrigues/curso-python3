# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    # Se ele ainda vai se alistar ao exército militar
    # Se é a hora de se alistar
    # Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# Passo 1: Receber um valor para "ano de nascimento"
ano_nascimento = int(input('Em que ano você nasceu? '))

# Passo 2: Criar uma condição aninhada para exibir o status de alistamento e o tempo restante/de atraso
idade = 2025 - ano_nascimento
if idade == 18:
    print(f'Você está com {idade} anos, já é hora de se alistar.')
elif idade < 18:
    tempo_restante = 18 - idade
    print(f'Você está com {idade} anos, deverá se alistar daqui a {tempo_restante} anos.')
else:
    tempo_perdido = idade - 18
    print(f'Você está com {idade} anos, o prazo para o alistamento já passou há {tempo_perdido} anos.')
# ----------------------------------------------------------------------------------------------------| Desafio [039]
