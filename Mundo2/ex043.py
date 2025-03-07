# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
    # Abaixo de 18.5: Abaixo do Peso
    # Entre 18.5 e 25: Peso ideal
    # 25 até 30: Sobrepeso
    # 30 até 40: Obesidade
    # Acima de 40: Obesidade mórbida

cores = {'limpa':'\033[m', 'pretoebranco':'\033[7;40m', 'negritoazul':'\033[1;34m', 'negritoroxo':'\033[1;35m'}

# Passo 1: Receber valores para "peso" e "altura"
peso = float(input(f"{cores['pretoebranco']}Digite o seu peso: (kg){cores['limpa']} "))
altura = float(input(f"{cores['pretoebranco']}Digite a sua altura: (m){cores['limpa']} "))
print(f"{cores['negritoroxo']}Você pesa {peso} kg e tem {altura} m de altura.{cores['limpa']}")

# Passo 2: Exibir o status da pessoa, de acordo com o seu IMC
imc = peso / altura ** 2
if imc < 18.5:
    print(f"{cores['negritoazul']}Seu IMC está em {imc:.1f}, de acordo com isso você está abaixo do peso.{cores['limpa']}")
elif imc < 25:
    print(f"{cores['negritoazul']}Seu IMC está em {imc:.1f}, de acordo com isso você está com o peso ideal.{cores['limpa']}")
elif imc < 30:
    print(f"{cores['negritoazul']}Seu IMC está em {imc:.1f}, de acordo com isso você está com sobrepeso.{cores['limpa']}")
elif imc < 40:
    print(f"{cores['negritoazul']}Seu IMC está em {imc:.1f}, de acordo com isso você está com obesidade.{cores['limpa']}")
else:
    print(f"{cores['negritoazul']}Seu IMC está em {imc:.1f}, de acordo com isso você está com obesidade mórbida.{cores['limpa']}")
# -------------------------------------------------------------------------------------------------------------------------------| Desafio [043]
