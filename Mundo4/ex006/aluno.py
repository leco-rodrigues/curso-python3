from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, curso: str, turma: str) -> None:
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self) -> None:
        print(f"{self.nome} acabou de fazer matrícula")
