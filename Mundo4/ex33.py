# Classes Aluno e Professor:
    # Implemente a seguinte estrutura de diagrama de classes.
        # classe Pessoa (abstract)
        # _nome
        # _nascimento
        # @nascimento
        # @idade
        # classe Aluno(Pessoa)
        # cursos_oficiais
        # _curso
        # @curso
        # add_curso(curso)

from abc import ABC
import datetime
from rich import print, inspect


def ano_valido(ano: int) -> bool:
    ano_atual: int = datetime.datetime.now().year
    if ano > ano_atual or ano < (ano_atual - 120):
        return False
    return True


# Passo 1: Criar classe Pessoa(abstract)
class Pessoa(ABC):
    def __init__(self, nome: str, nasc: int) -> None:
        self._nome = nome
        if ano_valido(nasc):
            self._nascimento = nasc
        else:
            raise ValueError(f"Ano {nasc} é inválido")

    @property
    def nascimento(self) -> int:
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano: int) -> None:
        if ano_valido(ano):
            self._nascimento = ano
        else:
            raise ValueError(f"Ano {ano} é inválido")

    @property
    def idade(self) -> int:
        ano_atual: int = datetime.datetime.now().year
        return ano_atual - self._nascimento

    @idade.setter
    def idade(self, valor: int) -> None:
        raise PermissionError("Você não pode alterar a idade. Mude o ano de nascimento")

# Passo 2: Criar classe Aluno(Pessoa)
class Aluno(Pessoa):
    cursos_oficiais: list[str] = ["ADM", "ADS", "ENG", "CONT"]

    def __init__(self, nome: str, nasc: int, curso: str) -> None:
        super().__init__(nome, nasc)
        if curso not in self.cursos_oficiais:
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais")
        self._curso = curso

    @property
    def curso(self) -> str:
        return self._curso

    @curso.setter
    def curso(self, curso: str) -> None:
        if curso in self.cursos_oficiais:
            self._curso = curso
        else:
            raise ValueError(f"O curso {curso} não está na lista de cursos oficiais")

# Passo 3: Criar método add_curso(curso)
    def add_curso(self, curso: str) -> None:
        if curso not in self.cursos_oficiais:
            self.cursos_oficiais.append(curso)
        else:
            raise ValueError(f"O curso {curso} já está na lista de cursos oficiais")

# Passo 4: Exibir o resultado
a1: Aluno = Aluno("Alex", 1999, "ADM")
# a1: Aluno = Aluno("Alex", 1999, "KKK")

a1.add_curso("MODA")
# a1.idade = 45
# a1.nascimento = 2029
# a1.nascimento = 1620
a1.nascimento = 2010
a1.curso = "MODA"

inspect(a1, private=True, methods=True)
# -| AULA 12 - DOMINE ENCAPSULAMENTO EM PYTHON COM GETTERS, SETTERS E 6 PROJETOS REAIS | DESAFIO 33
