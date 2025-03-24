# Contando vogais em Tupla:
    # Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
    # Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# Passo 1: Criar uma tupla com "palavras"
words: tuple = ("my", "name", "is", "i", "do", "not", "remember")

# Passo 2: Exibir as vogais de cada palavra
vogals: tuple = ("a", "e", "i", "o", "u")

for i, word in enumerate(words):
    if word.split() in vogals:
        print(word)

# Passo 3: Exibir mensagem de encerramento
print("\nExiting program... Thank you for using it! 😄")
# ------------------------------------------------------| AULA 16 - TUPLAS | DESAFIO [077]
