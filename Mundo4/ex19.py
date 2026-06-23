# Crie uma classe Livro, que vai simular a passagem de páginas de um livro,
# considerando também se o usuário chegou até o fim da história.

from rich import print

# Passo 1: Criar classe Livro
class Livro:
    pagina: int = 1
    
    def __init__(self, titulo: str, paginas: int):
        self.titulo = titulo
        self.paginas = paginas
        print(f"""
:book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} páginas[/] no total.
Você agora está na[/] [yellow]página {self.pagina}[/]
              """)

# Passo 2: Criar um método para simular a passagem de páginas
    def avancar_paginas(self, paginas: int):
        cont: int = 0
        for i in range(1, paginas + 1):
            Livro.pagina += 1
            cont += 1

            print(f"Pág{self.pagina} ▶", end = " ")

            if  Livro.pagina >= self.paginas:
                break

        print(f"[blue]Você avançou {cont} páginas e agora está na[/] [yellow]página {Livro.pagina}[/]")

        if Livro.pagina == self.paginas:
            print(f":closed_book: [red]Você chegou ao final do livro {self.titulo}[/]")

# Passo 3: Exibir o resultado
l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)

# -| AULA 06 - APRENDA PROGRAMAÇÃO ORIENTADA A OBJETOS COM DESAFIOS EM PYTHON | DESAFIO 19
