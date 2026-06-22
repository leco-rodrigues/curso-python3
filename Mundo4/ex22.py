# Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples
# (canal, volume e liga/desliga).

from rich import print
from rich.panel import Panel

# Passo 1: Criar classe ControleRemoto
class ControleRemoto:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = 2

        while True:
            if not self.ligada:
                print(Panel("[red]A TV está desligada[/]", title = "[ TV ]", width = 30))
            elif self.ligada:
                volume: str = "VOLUME = [white on green]  [/][white on white]   [/]"

                if self.volume == 0:
                    volume = "VOLUME = [white on green][/][white on white]     [/]"
                if self.volume == 1:
                    volume = "VOLUME = [white on green] [/][white on white]    [/]"
                elif self.volume == 3:
                    volume = "VOLUME = [white on green]   [/][white on white]  [/]"
                elif self.volume == 4:
                    volume = "VOLUME = [white on green]    [/][white on white] [/]"
                elif self.volume == 5:
                    volume = "VOLUME = [white on green]     [/][white on white][/]"

                if self.canal == 1:
                    print(Panel(f"CANAL  = [white on yellow] 1 [/] 2  3  4  5\n{volume}", width = 30))
                elif self.canal == 2:
                    print(Panel(f"CANAL  =  1 [white on yellow] 2 [/] 3  4  5\n{volume}", width = 30))
                elif self.canal == 3:
                    print(Panel(f"CANAL  =  1  2 [white on yellow] 3 [/] 4  5\n{volume}", width = 30))
                elif self.canal == 4:
                    print(Panel(f"CANAL  =  1  2  3 [white on yellow] 4 [/] 5\n{volume}", width = 30))
                elif self.canal == 5:
                    print(Panel(f"CANAL  =  1  2  3  4 [white on yellow] 5 [/]\n{volume}", width = 30))

            controle: str = input(f"< CH{self.canal} > - VOL{self.volume} + ")

            if controle == "@":
                if self.ligada:
                    self.ligada = False
                elif not self.ligada:
                    self.ligada = True

            if controle == ">" and self.ligada:
                if self.canal == 5:
                    self.canal = 1
                else:
                    self.canal += 1

            if controle == "<" and self.ligada:
                if self.canal == 1:
                    self.canal = 5
                else:
                    self.canal -= 1

            if controle == "+" and self.ligada:
                if self.volume == 5:
                    pass
                else:
                    self.volume += 1

            if controle == "-" and self.ligada:
                if self.volume == 0:
                    pass
                else:
                    self.volume -= 1

# Passo 2: Exibir o resultado
c1 = ControleRemoto()

# -| AULA 06 - APRENDA PROGRAMAÇÃO ORIENTADA A OBJETOS COM DESAFIOS EM PYTHON | DESAFIO 22
