# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# Passo 1: Receber valores para duas "notas"
nota1 = float(input('\033[7;40mDigite a primeira nota do aluno:\033[m '))
nota2 = float(input('\033[7;40mDigite a segunda nota do aluno:\033[m '))

# Passo 2: Exibir a média
print(f'\033[1;34mA nota média do aluno foi {(nota1 + nota2) / 2:.1f}.\033[m')
# ---------------------------------------------------------------------------| Desafio [007]
