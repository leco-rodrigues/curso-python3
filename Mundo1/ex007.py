# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m'}
# Passo 1: Receber valores para duas "notas"
nota1 = float(input(f'{cores['pretoebranco']}Digite a primeira nota do aluno:{cores['limpa']} ')) # primeira nota
nota2 = float(input(f'{cores['pretoebranco']}Digite a segunda nota do aluno:{cores['limpa']} ')) # segunda nota

# Passo 2: Calcular e exibir a média
print(f'{cores['negritoazul']}A nota média do aluno foi {(nota1 + nota2) / 2:.1f}.{cores['limpa']}') # média = (nota1 + nota2) / 2
# -------------------------------------------------------------------------------------------------| Desafio [007]
