from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome: str, idade: int, especialidade: str, nivel: str) -> None:
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self) -> None:
        print(f"Prof. {self.nome} começou a dar aula")
