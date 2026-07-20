# Máquina de café:
    # Simule uma cafeteria orientada a objetos
        # BebidaQuente (abstract) + preparar() + ferver_agua() + misturar() (abstract) + servir() (abstract)
        # Cafe + misturar() + servir()
        # Cha + misturar() + servir()
        # Leite + misturar() + servir()

from abc import ABC, abstractmethod

# Passo 1: Criar classe abstrata BebidaQuente
class BebidaQuente(ABC):
    

# Passo 2: Criar método preparar()
    def preparar(self) -> None:
        print(f"""
--- Iniciando o Preparo ---
1. {self.ferver_agua()}
2. {self.misturar()}
3. {self.servir()}
--- Bebida Pronta ---
              """)

# Passo 3: Criar método ferver_agua()
    def ferver_agua(self) -> str:
        return "Fervendo água a 100 graus Celsius."

# Passo 4: Criar método asbtrato misturar()
    @abstractmethod
    def misturar(self) -> str:
        pass

# Passo 5: Criar método abstrato servir()
    @abstractmethod
    def servir(self) -> str:
        pass

# Passo 6: Criar subclasse Cafe
class Cafe(BebidaQuente):


    def misturar(self) -> str:
        return "Passando água pressurizada pelo pó de café moído."

    def servir(self) -> str:
        return "Servindo em xícara pequena."

# Passo 7: Criar subclasse Cha
class Cha(BebidaQuente):


    def misturar(self) -> str:
        return "Mergulhando o sachê de ervas na água."

    def servir(self) -> str:
        return "Servindo na caneca de porcelana com limão."

# Passo 8: Criar subclasse Leite
class Leite(BebidaQuente):


    def misturar(self) -> str:
        return "Passando vapor pressurizado pelo bico do leite."

    def servir(self) -> str:
        return "Servindo na caneca grande, já com café."

# Passo 9: Exibir o resultado
bebida = Cafe()
bebida.preparar()

# -| AULA 09 - DESAFIOS DE HERANÇA, ABSTRAÇÃO E CLASSES | DESAFIO 24
