# Analisano e gerando Dicionários:
    # Faça um programa que tenha um função chamada notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
        # - Quantidade de notas
        # - A maior nota
        # - A menor nota
        # - A média da turma
        # - A situação (opcional)
    # Adicione também as docstrings da função.

def display_exit_message(message: str = None) -> None:
    if (not message):
        message = "Exiting program... Thanks for using it! 😄"
    print(message)


# Passo 1: 
def notas(*notas: float, situacao: bool = False) -> dict[str: object]:
    """
    -> Cria e retorna um dicionário com dados baseados nas notas fornecidas.

    Parâmetros:
        :notas: tupla contendo todas as notas fornecidas
        :situacao: valor booleano para exibir ou não a situação da média da turma

    Returns:
        dict[str: object]: dicionário contendo todos os dados
    """
    total_notas: float = len(notas)
    maior_nota: float = max(notas)
    menor_nota: float = min(notas)
    soma_notas: float = 0
    for nota in notas:
        soma_notas += nota
    media_turma = soma_notas / total_notas
    media_turma_formatada = f"{media_turma:.2f}"

    notas_dict: dict[str: object] = {}
    notas_dict["Total"] = total_notas
    notas_dict["Maior"] = maior_nota
    notas_dict["Menor"] = menor_nota
    notas_dict["Média"] = media_turma_formatada

    if situacao:
        if media_turma >= 8:
            situacao_turma: str = "Ótima"
        elif media_turma >= 6:
            situacao_turma = "Boa"
        else:
            situacao_turma = "Ruim"
        notas_dict["Situação"] = situacao_turma

    return notas_dict


# Passo 2: Exibir o resultado
print(notas(5.5, 2.5, 1.5, situacao=True))

# Passo 3: Exibir mensagem de encerramento
display_exit_message()
# -------------------| AULA 21 - FUNÇÕES (PARTE 2) | DESAFIO [105]
