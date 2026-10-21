# Criptografia de senhas com SHA-256:
    # Crie uma classe que gerencie a hash SHA256 de uma senha.
        # classe Credencial
        # @senha
        # __hash
        # validar(chave)
from hashlib import sha256
from rich import print, inspect


# Passo 1: Criar classe Credencial
class Credencial:
    def __init__(self) -> None:
        self.__hash: str | None = None

    @property
    def senha(self) -> str:
        raise PermissionError("A senha não deve ser revelada!")

    @senha.setter
    def senha(self, chave: str) -> None:
        if len(chave) > 8 and len(chave) < 16:
            self.__hash = sha256(chave.encode("utf-8")).hexdigest()
        else:
            raise ValueError("Senha inválida. Sua senha deve ter entre 8 e 16 caracteres!")

# Passo 2: Criar método validar(chave)
    def validar(self, chave: str) -> bool:
        hash_chave: str = sha256(chave.encode("utf-8")).hexdigest()
        if hash_chave == self.__hash:
            print("Senha confere!\n[green]True[/]")
            return True
        else:
            print("Senha não bate!\n[red]False[/]")
            return False

# Passo 3: Exibir o resultado
c: Credencial = Credencial()
c.senha = str(input("Digite a senha: "))

c.validar("Teste")
inspect(c, private=True, methods=True)
# -| AULA 12 - DOMINE ENCAPSULAMENTO EM PYTHON COM GETTERS, SETTERS E 6 PROJETOS REAIS | DESAFIO 30
