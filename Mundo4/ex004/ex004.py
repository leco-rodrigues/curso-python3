from rich import print, inspect

class Pessoa:
    def __init__(self, nome: str = "", idade: int = 0) -> None:
         self.nome = nome
         self.idade = idade

    def fazer_aniversario(self) -> None:
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, curso: str, turma: str) -> None:
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self) -> None:
        print(f"{self.nome} acabou de fazer matrícula")


class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, especialidade: str, nivel: str) -> None:
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self) -> None:
        print(f"Prof. {self.nome} começou a dar aula")


class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, cargo: str, setor: str) -> None:
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self) -> None:
        print(f"{self.nome} acabou de bater ponto.")


a1: Aluno = Aluno("José", 17, "Informática", "T01")
a1.fazer_aniversario()
a1.fazer_matricula()
#inspect(a1, methods = True)

p1: Professor = Professor("Samuel", 37, "Biologia", "Mestrado")
p1.fazer_aniversario()
p1.dar_aula()
#inspect(p1, methods = True)

f1: Funcionario = Funcionario("Cláudia", 27, "Secretária", "Secretaria")
f1.fazer_aniversario()
f1.bater_ponto()
inspect(f1, methods = True)
