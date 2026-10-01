# Diário Secreto:
    # Simule um diário secreto orientado a objetos.
        # classe Diario
        # __segredos[]
        # __senha
        # escrever(msg)
        # ler(senha)
from rich import print


# Passo 1: Criar classe Diario
class Diario:
    def __init__(self, senhaMestra: str = "123") -> None:
        self.__senha = senhaMestra
        self.__segredos: list[str] = []

    @property
    def senha(self) -> None:
        raise PermissionError("Ninguém tem permissão de ver a senha")

# Passo 2: Criar método escrever(msg)
    def escrever(self, msg: str) -> None:
        self.__segredos.append(msg)

# Passo 3: Criar método ler(senha)
    def ler(self, senha: str) -> None:
        if senha == self.__senha:
            conteudo: str = "\n- ".join(self.__segredos)
            print(f"""
[green]Diário LIBERADO![/]
- {conteudo}
                  """)
        else:
            raise PermissionError("Senha inválida! Você não pode ler meu diário!")

# Passo 4: Exibir o resultado
d: Diario = Diario("Python")

d.escrever("Primeira mensagem")
d.escrever("Você é uma pessoa simpática")
d.escrever("Você gosta de Python")

d.ler("Python")
# -| AULA 12 - DOMINE ENCAPSULAMENTO EM PYTHON COM GETTERS, SETTERS E 6 PROJETOS REAIS | DESAFIO 29
