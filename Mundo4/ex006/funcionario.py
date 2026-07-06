from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome: str, idade: int, cargo: str, setor: str) -> None:
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self) -> None:
        print(f"{self.nome} acabou de bater ponto.")
