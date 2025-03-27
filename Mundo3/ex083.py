# Validando expressões matemáticas
    # Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
    # Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

# Passo 1: Solicitar um valor para "expressão" (com parênteses)
phrase: str = str(input("Enter a mathematical expression: "))

# Passo 2: Exibir se os parênteses estão abertos e fechados corretamente
if (phrase.count("(") == phrase.count(")")):
    print("That's a valid expression.")
else:
    print("That's not a valid expression.")

# Passo 3: Exibir mensagem de encerramento
print("Exiting program... Thank you for using it! 😄")
# ----------------------------------------------------| AULA 17 - LISTAS (PARTE 1) | DESAFIO [083]
