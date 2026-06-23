# Crie a classe Caneta, que simule o funcionamento de uma caneta colorida,
# podendo escrever frases na cor relativa.

from rich import print

# Passo 1: Criar classe Caneta
class Caneta:
    def __init__(self, cor: str):
        self.cor = cor
        self.tampada: bool = True

# Passo 2: Criar método para destampar
    def destampar(self):
        self.tampada = False

# Passo 3: Criar método para escrever
    def escrever(self, texto:str):
        cores: dict[str, str] = {"azul":"blue", "vermelho":"red", "verde":"green"}

        if self.tampada:
            print(f"A {cores[self.cor]}caneta[/] está tampada.")
        else:
            print(f"[{cores[self.cor]}]{texto}[/]", end = "")

# Passo 4: Criar método para quebrar linha
    def quebrar_linha(self, numero: int):
        for i in range(1, numero):
            print("\n")

# Passo 5: Exibir o resultado
c1 = Caneta("azul")
c2 = Caneta("vermelho")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem? ")
c1.quebrar_linha(2)
c2.escrever("Olá, Gafanhoto! ")
c3.escrever("Vamos exercitar!")

# -| AULA 06 - APRENDA PROGRAMAÇÃO ORIENTADA A OBJETOS COM DESAFIOS EM PYTHON | DESAFIO 21
