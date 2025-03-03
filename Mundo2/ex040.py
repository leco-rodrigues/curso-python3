# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
    # Média abaixo de 5.0: REPROVADO
    # Média entre 5.0 e 6.9: RECUPERAÇÃO
    # Média 7.0 ou superior: APROVADO

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}

# Passo 1: Receber valores para duas "notas"
nota1 = float(input(f"{cores['pretoebranco']}Qual foi a primeira nota do aluno?{cores['limpa']} "))
nota2 = float(input(f"{cores['pretoebranco']}Qual foi a segunda nota do aluno?{cores['limpa']} "))

# Passo 2: Exibir se está aprovado, reprovado ou em recuperação
media = (nota1 + nota2) / 2 
if media >= 7.0:
    print(f"{cores['negritoazul']}Sua média foi {media}. Você está APROVADO! Parabéns!{cores['limpa']}")
elif 6.9 >= media >= 5.0:
    print(f"{cores['negritoazul']}Sua média foi {media}. Você está em RECUPERAÇÃO! Estude mais!{cores['limpa']}")
else:
    print(f"{cores['negritoazul']}Sua média foi {media}. Você está REPROVADO! Se esforce mais na próxima!{cores['limpa']}")
# ------------------------------------------------------------------------------------------------------------------------| Desafio [040]
