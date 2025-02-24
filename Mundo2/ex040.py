# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
    # Média abaixo de 5.0: REPROVADO
    # Média entre 5.0 e 6.9: RECUPERAÇÃO
    # Média 7.0 ou superior: APROVADO

# Passo 1: Receber dois valores para duas "notas"
nota1 = float(input('Qual foi a primeira nota do aluno? ')) # primeira nota
nota2 = float(input('Qual foi a segunda nota do aluno? ')) # segunda nota

# Passo 2: Calcular a média e criar uma condição aninhada para exibir se está aprovado, reprovado ou em recuperação
media = (nota1 + nota2) / 2 
if media >= 7.0: # condição para aprovação
    print(f'Sua média foi {media}. Você está APROVADO! Parabéns!')
elif 6.9 >= media >= 5.0: # condição para recuperação
    print(f'Sua média foi {media}. Você está em RECUPERAÇÃO! Estude mais!')
else: # reprovação
    print(f'Sua média foi {media}. Você está REPROVADO! Se esforce mais na próxima!')
# ----------------------------------------------------------------------------------| Desafio [040]
