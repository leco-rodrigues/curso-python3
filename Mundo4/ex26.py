# Sistema de cálculo de salário:
    # Crie a estrutura capaz de calcular salários de funcionários diferentes
        # Funcionario (abstract) + nome + sal_bruto + salario + sal_min = 1621 + inss = 7.5 + calc_sal() (abstract) + analisar_sal()
        # Horista + valor_hora + horas_trab + calc_sal()
        # Mensalista + calc_sal()

from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

# Passo 1: Criar classe abstrata Funcionario
class Funcionario(ABC):
    salario_minimo: float = 1_612
    desconto_inss: float = 7.5

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.salario_bruto: float = 0
        self.salario: float = 0

# Passo 2: Criar método abstrato calc_sal()
    @abstractmethod
    def calcular_salario(self) -> float:
        pass

# Passo 3: Criar método analisar_sal()
    def analisar_salario(self) -> None:
        qtd_salarios_min: float = self.calcular_salario() / self.salario_minimo
        conteudo: str = f"O salário de [blue]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) é de [green]R${self.calcular_salario():.2f}[/] e corresponde a [yellow]{qtd_salarios_min:.1f} salários mínimos[/]."
        print(Panel(conteudo, title = "Análise de Salário", width = 45))

# Passo 4: Criar subclasse Horista
class Horista(Funcionario):
    def __init__(self, nome: str, valor_hora: float = 7.37, horas_trabalhadas: float = 220) -> None:
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas
        self.salario_bruto = self.valor_hora * self.horas_trabalhadas

    def calcular_salario(self) -> float:
        valor_desconto: float = (self.salario_bruto * Funcionario.desconto_inss) / 100
        self.salario = self.salario_bruto - valor_desconto
        return self.salario

# Passo 5: Criar subclasse Mensalista
class Mensalista(Funcionario):
    def __init__(self, nome: str, salario_bruto: float = Funcionario.salario_minimo) -> None:
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    def calcular_salario(self) -> float:
        valor_desconto: float = (self.salario_bruto * self.desconto_inss) / 100
        self.salario = self.salario_bruto - valor_desconto
        return self.salario
        

# Passo 6: Exibir o resultado
f1: Horista = Horista("Paulo", 12, 200)
f1.calcular_salario()
f1.analisar_salario()

f2: Mensalista = Mensalista("Amanda", 9500)
f2.calcular_salario()
f2.analisar_salario()

# -| AULA 09 - DESAFIOS DE HERANÇA, ABSTRAÇÃO E CLASSES | DESAFIO 26
