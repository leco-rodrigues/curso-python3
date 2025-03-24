# Lista de Preços com Tupla:
    # Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
    # No final, mostre uma listagem de preços, organizando os dados em forma de tabular.

# Passo 1: Criar uma tupla com "nomes" e "preços"
products_prices: tuple[str, float, ...] = ( # type: ignore
    "Cerveja", 1.49, "Refrigerante", 4.99, "Arroz", 8.28, "Leite", 2.65, "Água Sanitária", 1.99,
    "Ovos", 8.49, "Achocolatado", 4.98, "Salgadinhos", 0.69, "Sabão em Pó", 8.49, "Fraldinha", 16.98
)

# Passo 2: Exibir em forma tabular
print(f"\t{' MALL ':=^40}\n")

for i in range(0, len(products_prices), 2):
    print(f"{products_prices[i]:.<30}R${products_prices[i + 1]:>7.2f}")

# Passo 3: Exibir mensagem de encerramento
print("\nExiting program... Thank you for using it! 😄")
# ------------------------------------------------------| AULA 16 - TUPLAS | DESAFIO [076]
