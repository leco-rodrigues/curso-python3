# Criando Funcionários com Herança e Polimorfismo:
    # Crie a seguinte estrutura de classes para calcular bônus salarial.
        # Funcionario(abstract)
        # + nome
        # - __salário
        # + calcular_bonus()
        # Gerente(Funcionario) | bônus 15%
        # Designer(Funcionario) | bônus 8%
        # Desenvolvedor(Funcionario) | bônus 10%
from abc import ABC, abstractmethod


def validar_salario(valor: int | float) -> bool:
    if isinstance(valor, (int, float)) and not isinstance(valor, bool):
        return valor >= 1621:
    return False


# Passo 1: Criar classe Funcionario(abstract)
class Funcionario(ABC):
    def __init__(self, nome: str | None = None, salario: float = 1621) -> None:
        self.nome = nome
        if validar_salario(salario):
            self.__salario = salario
        else:
            raise ValueError(f"O valor '{salario}' não é válido como salário.")

    @property
    def salario(self) -> float:
        return self.__salario

    @salario.setter
    def salario(self, valor: float) -> None:
        if validar_salario(valor):
            if valor >= self.__salario:
                self.__salario = valor
            else:
                raise ValueError("Você não pode reduzir o salário de um funcionário.")
        else:
            raise ValueError(f"O valor '{valor}' não é válido como salário.")

    def __str__(self) -> str:
        return f"{self.nome} ganha R${self.salario:,.2f} e por ser {self.__class__.__name__} o bônus será de R${self.calcular_bonus():,.2f}."

# Passo 2: Criar método polimórfico calcular_bonus()
    @abstractmethod
    def calcular_bonus(self) -> float:
        pass

# Passo 3: Criar classe Gerente(Funcionario)
class Gerente(Funcionario):
    def calcular_bonus(self) -> float:
        return self.salario * 0.15

# Passo 4: Criar classe Designer(Funcionario)
class Designer(Funcionario):
    def calcular_bonus(self) -> float:
        return self.salario * 0.08

# Passo 5: Criar classe Desenvolvedor(Funcionario)
class Desenvolvedor(Funcionario):
    def calcular_bonus(self) -> float:
        return self.salario * 0.10

# Passo 6: Exibir o resultado
f1: Designer = Designer("Pedro", 1_800)
f2: Gerente = Gerente("Paulo", 3_000)
f3: Desenvolvedor = Desenvolvedor("Alex", 2_500)
# f4: Gerente = Gerente("Paulo", -500)
# f5: Desenvolvedor = Desenvolvedor("Alex", 1500)
# f6: Designer = Designer("Paulo", "Dois mil")

# f1.salario = 1000
f1.salario = 2000

print(f1)
print(f2)
print(f3)
print(f1.calcular_bonus())
print(f2.calcular_bonus())
print(f3.calcular_bonus())
# -| AULA 15 - 7 DESAFIOS DE POLIMORFISMO EM PTYHON | DESAFIO 34
