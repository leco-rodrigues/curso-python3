# Validando expressões matemáticas
    # Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
    # Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

# Passo 1: Solicitar um valor para "expressão" (com parênteses)
while True:
    math_expression: str = str(input("Enter a mathematical expression: ")).strip()

    if math_expression and (math_expression.count("(") or math_expression.count(")")):
        break
    else:
        print("Invalid input! Please enter a valid expression.")

# Passo 2: Exibir se os parênteses estão abertos e fechados corretamente
balance: int = 0

for i in math_expression:
    if i == "(":
        balance += 1
    elif i == ")":
        balance -= 1
        if balance < 0:
            print("That's not a valid expression.")
            break

else:
    print("That's a valid expression." if balance == 0 else "That's not a valid expression.")

# Passo 3: Exibir mensagem de encerramento
print("Exiting program... Thank you for using it! 😄")
# ----------------------------------------------------| AULA 17 - LISTAS (PARTE 1) | DESAFIO [083]
