from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome: str) -> None:
        self.nome = nome

    @abstractmethod
    def emitir_som(self) -> None:
        pass

class Pato(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def emitir_som(self) -> None:
        print(f"{self.nome} acabou de dizer 'QUACK! QUACK!'")

class Cachorro(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def emitir_som(self) -> None:
        print(f"{self.nome} acabou de dizer 'AU! AU! AU!'")

class Spitz(Cachorro):
    def emitir_som(self) -> None:
        print(f"{self.nome} acabou de dizer 'au!au!au!au!au!au!au!au!au!'")

class PitBull(Cachorro):
    def emitir_som(self) -> None:
        print(f"{self.nome} acabou de dizer 'RUF! RUF! RUF!'")

class Gato(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def emitir_som(self) -> None:
        print(f"{self.nome} acabou de dizer 'MIAU! MIAU!'")
    
class Galinha(Animal):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def emitir_som(self) -> None:
        print(f"{self.nome} acabou de dizer 'PÓ! PÓ! PÓ!'")
