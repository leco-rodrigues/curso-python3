# Função que calcula área:
    # Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def show_exit_message(message: str = None) -> None:
    if message is None:
        message = "\n----------\nExiting program... Thanks for using it! 😄\n----------\n"
    print(message)


# Passo 1: Criar função para calcular a "área" a partir da "largura" e "comprimento"
def area(largura: float, comprimento: float) -> float:
    area_: float = largura * comprimento
    return area_


def input_medida(message: str = "Digite a medida:") -> float:
    prompt: str = message.strip() + " "
    while True:
        try:
            medida: str = str(input(prompt))
            if not (medida):
                raise ValueError("Campo vazio")
            if (medida.startswith(".")) or (medida.endswith(".")) or not all(c.isdigit() for c in medida.replace(".", "", 1)):
                    raise ValueError(f"O valor '{medida}' é inválido, valores não numéricos não são aceitos")
            if (float(medida) <= 0):
                raise ValueError(f"O valor '{medida}' é inválido, 0 e valores negativos não são aceitos")
            return float(medida)
        except ValueError as vE:
            print(f"\n-------\nEntrada inválida: {vE}. Por favor, insira um valor numérico positivo.\n-------\n")


# Passo 2: Solicitar valores para "largura" e "comprimento"
print("\n----------\nCALCULAR A ÁREA DE UM TERRENO\n----------\n")

largura_terreno = input_medida("Digite a largura (m) do terreno:")
comprimento_terreno = input_medida("Digite o comprimento (m) do terreno:")

# Passo 3: Exibir tamanho da "área"
area_terreno = area(largura_terreno, comprimento_terreno)

print(f"\n-------\n\nA área de um terreno com {largura_terreno}m x {comprimento_terreno}m é igual a {area_terreno}m².")

# Passo 4: Exibir mensagem de encerramento:
show_exit_message()
# ----------------| AULA 21 - FUNÇÕES (PARTE 1) | DESAFIO [096]
