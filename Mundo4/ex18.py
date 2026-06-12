# Crie a classe Churrasco, onde seja prossível informar quantas pessoas vão participar e
# mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.
# Considere:
    # Consumo padrão: 400g pessoa
    # Preço: R$82,40/Kg

from rich import print
from rich.panel import Panel

# Passo 1: Criar a classe Churrasco
class Churrasco:
    CONS_PESSOA: float = 0.4
    PRECO: float = 82.40
    
    def __init__(self, titulo: str, quant: int):
        self.titulo = titulo
        self.quant = quant

# Passo 2: Criar um método para analisar o necessário de carne, o custo total e por pessoa
    def analise(self):
        quant_carne: float = self.CONS_PESSOA * self.quant
        custo_total: float = self.PRECO * quant_carne
        custo_pessoa: float = custo_total / self.quant

        caixa = Panel(f"""
Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidado{'s' if self.quant > 1 else ''}[/]
Cada participante comerá {self.CONS_PESSOA}Kg e cada Kg custa R${self.PRECO:.2f}
Recomendo [blue]comprar {quant_carne:.3f}Kg[/] de carne
O custo total será de [green]R${custo_total:.2f}[/]
Cada pessoa pagará [yellow]R${custo_pessoa:.2f}[/] para participar.
                      """, title=self.titulo, width=60)

        return caixa

# Passo 3: Exibir o resultado
c1 = Churrasco("Churras dos Amigos", 15)
print(c1.analise())

# -| AULA 06 - Aprenda Programação Orientada a Objetos com Desafios em Python | DESAFIO 18
