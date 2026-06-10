# Crie uma classe Funcionario, onde podemos cadastrar nome, setor e cargo.
# Crie também um método que permita ao funcionário se apresentar.

from rich import print

# Passo 1: Criar a classe Funcionario
class Funcionario:
    empresa: str = "Curso em Video"

    def __init__(self, nome: str, setor: str, cargo: str):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

# Passo 2: Criar um método de apresentação do funcionário
    def apresentar(self):
        return f":wave: Olá, meu nome é [blue]{self.nome}[/] e trabalho como [blue]{self.cargo}[/] no setor de [blue]{self.setor}[/] da empresa [blue]{self.empresa}[/]."

# Passo 3: Exibir o resultado
f1 = Funcionario("Alex", "TI", "Programador")
print(f1.apresentar())

f2 = Funcionario("Julia", "Administração", "Diretora")
print(f2.apresentar())

# -| AULA 06 - APRENDA PROGRAMAÇÃO ORIENTADA A OBJETOS COM DESAFIOS EM PYTHON | DESAFIO 16
