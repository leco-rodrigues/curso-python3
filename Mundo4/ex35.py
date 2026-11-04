# Simulando Arquivos PDF e DOC com Polimorfismo:
    # Crie um simulador que gerencie a abertura de diferentes tipos de arquivos
    # Arquivo(abstract)
    # + nome
    # # _extensao
    # + tamanho
    # + @nome_completo
    # + abrir()
    # PDF(Arquivo)
    # DOC(Arquivo)
from abc import ABC, abstractmethod


# Passo 1: Criar classe Arquivo(abstract)
class Arquivo(ABC):
    def __init__(self, nome: str, tam: int) -> None:
        self.nome = nome
        self._extensao = None
        self.tamanho = tam

    @property
    def extensao(self) -> None | str:
        return self._extensao

    @property
    def nome_completo(self) -> str:
        return f"'{self.nome}.{self.extensao}'({self.tamanho * 0.000001}MB)"

    @nome_completo.setter
    def nome_completo(self, _: str) -> None:
        raise PermissionError("Você não tem permissão para alterar o 'nome completo' do arquivo dessa forma")

# Passo 2: Criar método abstrato polimórfico abrir()
    @abstractmethod
    def abrir(self) -> None:
        pass

# Passo 3: Criar classe PDF(Arquivo)
class PDF(Arquivo):
    def __init__(self, nome: str, tam: int) -> None:
        super().__init__(nome, tam)
        self._extensao = "pdf"

    def abrir(self) -> None:
        print(f"Abrindo o arquivo {self.nome_completo} no Adobe Reader")

# Passo 4: DOC(Arquivo)
class DOC(Arquivo):
    def __init__(self, nome: str, tam: int) -> None:
        super().__init__(nome, tam)
        self._extensao = "docx"
    
    def abrir(self) -> None:
        print(f"Abrindo o arquivo {self.nome_completo} no Microsoft Word")

def abrir_arquivo(obj: Arquivo) -> None:
    try:
        obj.abrir()
    except Exception as erro:
        print(f"Não foi possível abrir o arquivo: {erro}")

# Passo 5: Exibir o resultado
a1: DOC = DOC("prova", 250_000)
a2: PDF = PDF("contrato", 1_300_000)

abrir_arquivo(a1)
abrir_arquivo(a2)

print(a1.nome_completo)
print(a2.nome_completo)
# -| AULA 15 - 7 DESAFIOS DE POLIMORFISMO EM PTYHON | DESAFIO 35
