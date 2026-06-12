# Crie a classe Produto, onde podemos cadastrar nome e o preço.
# Crie também um método que mostre uma etiqueta de preço do produto.

from rich import print
from rich.panel import Panel

# Passo 1: Criar classe Produto
class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

# Passo 2: Criar um método para mostrar a etiqueta
    def etiqueta(self):
        caixa = Panel(f"{self.nome}\nR${self.preco:,.2f}", title="Produto", width=30, padding=(0,6))
        return caixa
        
# Passo 3: Exibir o resultado
p1 = Produto("Cadeira Gamer", 1_000.00)
print(p1.etiqueta())

p2 = Produto("Motorola G9 Play", 1_200.00)
print(p2.etiqueta())

# -| AULA 06 - APRENDA PROGRAMAÇÃO ORIENTADA A OBJETOS COM DESAFIOS EM PYTHON | DESAFIO 17
