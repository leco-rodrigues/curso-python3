from utils.colors import text_color
from utils.strings import error_message
from utils.numbers import leiaInt
from pathlib import Path

def menu(pergunta: str = "Sua opção:") -> int:
    print("-" * 26 + "\n" + "MENU".center(26) + "\n" + "-" * 26)
    print(f"{text_color('1', 'amarelo')} - {text_color('Ver lista de cadastros', 'azul')}")
    print(f"{text_color('2', 'amarelo')} - {text_color('Novo cadastro', 'azul')}")
    print(f"{text_color('3', 'amarelo')} - {text_color('Sair', 'azul')}")
    print("-" * 26)

    prompt: str = text_color(pergunta.strip(), "azul") + " "
    while True:
        try:
            escolha: int = int(input(prompt))
        except(ValueError, TypeError):
            error_message(text_color("ERRO: Por favor, digite uma opção válida.", "vermelho"))
        except(KeyboardInterrupt):
            error_message(text_color("\nO usuário decidiu interromper a ação.", "vermelho"))
            return 3
        else:
            if escolha in (1, 2, 3):
                return escolha
            else:
                error_message(text_color("ERRO: Por favor, digite uma opção válida.", "vermelho"))

def cadastrar() -> dict[str, object]:
    nome: str = input("Nome: ")
    idade: int = leiaInt("Idade: ")
    pessoa: dict[str, object] = {"nome": nome, "idade": idade}

    return pessoa

def adcionar_cadastro(nome: str, idade: int) -> None:
    caminho_arq: str = Path("C:/Users/alexr/OneDrive/Documentos/Meus Projetos/curso-python3/Mundo3/ex115/pessoas.txt")
    with caminho_arq.open("a", encoding = "utf-8") as arq:
        arq.write(f"{nome}, {idade} anos\n")

def exibir_cadastros() -> None:
    caminho_aqr: str = Path("C:/Users/alexr/OneDrive/Documentos/Meus Projetos/curso-python3/Mundo3/ex115/pessoas.txt")
    with caminho_aqr.open("r", encoding = "utf-8") as arq:
        conteudo: object = arq.read()
        print(conteudo)
