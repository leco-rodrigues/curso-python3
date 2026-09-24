class Avaliacao:
    def __init__(self, nome: str, disciplina: str, nota: float = 0) -> None:
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # Atributo protected (#)
    
    # Métodos Acessores    
    def get_nota(self) -> float: # Método Getter
        return self._nota
    
    def set_nota(self, valor: float) -> None: # Método Setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota inválida!")
