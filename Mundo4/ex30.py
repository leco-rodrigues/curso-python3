# Criptografia de senhas com SHA-256:
    # Crie uma classe que gerencie a hash SHA256 de uma senha.
        # classe Credencial
        # @senha
        # __hash
        # validar(chave)
import hashlib
from rich import print, inspect


# Passo 1: Criar classe Credencial
class Credencial:
    def __init__(self) -> None:
        self.__hash: str = hashlib.sha256("123".encode()).hexdigest()

    @property
    def senha(self) -> str:
        return self.__hash

    @senha.setter
    def senha(self, valor: str) -> None:
        self.__hash = hashlib.sha256(valor.encode()).hexdigest()

# Passo 2: Criar método validar(chave)
    def validar(self, chave: str) -> object:
        hash_chave: str = hashlib.sha256(chave.encode()).hexdigest()
        
        if hash_chave == self.__hash:
            return "Senha confere!\n[green]True[/]"
        else:
            return "Senha não bate!\n[red]False[/]"

# Passo 3: Exibir o resultado
c: Credencial = Credencial()
c.senha = str(input("Digite a senha: "))
print(c.validar("Teste"))

inspect(c, private=True, methods=True)
# -| AULA 12 - DOMINE ENCAPSULAMENTO EM PYTHON COM GETTERS, SETTERS E 6 PROJETOS REAIS | DESAFIO 30
