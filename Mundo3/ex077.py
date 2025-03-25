# Contando vogais em Tupla:
    # Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
    # Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# Passo 1: Criar uma tupla com "palavras"
words: tuple[str, ...] = ("My", "Name", "Is", "I", "Do", "Not", "Remember")

# Passo 2: Exibir as vogais de cada palavra
vowels: str = ("AaEeIiOoUu")

for word in words:
    vogal_list: list[str] = []

    for letter in word:
        if (letter in vowels) and (letter not in vogal_list):
            vogal_list.append(letter)
        
    if vogal_list:
        print(f"The word '{word}' has the vogal(s) '{', '.join(vogal_list).lower()}'.")
    else:
        print(f"The word '{word}' has no vowels.")

# Passo 3: Exibir mensagem de encerramento
print("\nExiting program... Thank you for using it! 😄")
# ------------------------------------------------------| AULA 16 - TUPLAS | DESAFIO [077]
