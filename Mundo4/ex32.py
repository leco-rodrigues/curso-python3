# Conta Bancária com Hash SHA-256
    # Aprimore o exercício de ContaBancaria, aplicando conceitos de encapsulamento.
        # classe ContaBancaria
        # _id
        # _titular
        # __saldo
        # __hash
        # @nome
        # validar_senha(chave)
        # pede_senha()
        # sacar(valor, chave)
        # depositar(valor)

import hashlib
import pwinput
from rich import inspect


def numero_nao_negativo(valor: float) -> bool:
    if type(valor) is float or type(valor) is int:
        if 0 <= valor:
            return True
        return False
    return False

def numero_inteiro(valor: float) -> bool:
    if type(valor) is int:
        return True
    return False

# Passo 1: Criar classe ContaBancaria
class ContaBancaria:
    def __init__(self, id: int, nome: str, saldo: float, chave: str | None = None) -> None:
        if numero_nao_negativo(id) and numero_inteiro(id):
            self._id = id
        else:
            raise ValueError("Número inválido para id")
        self._titular = nome
        if numero_nao_negativo(saldo):
            self.__saldo = saldo
        else:
            raise ValueError("Número inválido para saldo")
        if not chave:
            chave = self.pede_senha()
        self.__hash: str = hashlib.sha256(chave.encode()).hexdigest()
        
        print(f"Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")

    @property
    def nome(self) -> str:
        return self._titular

    @nome.setter
    def nome(self, nome: str) -> None:
        chave = self.pede_senha()
        if self.validar_senha(chave):
            self._titular = nome
            print(f"Titular da conta {self._id} atualizado com sucesso")
        else:
            print("Senha incorreta. Não foi possível alterar o titular da conta")

# Passo 2: Criar método validar_senha(chave)
    def validar_senha(self, chave: str) -> bool:
        if self.__hash == hashlib.sha256(chave.encode()).hexdigest():
            return True
        return False

# Passo 3: Criar método pede_senha()
    def pede_senha(self) -> str:
        chave: str = pwinput.pwinput("Senha: ", "*")
        return chave

# Passo 4: Criar método sacar(valor, chave)
    def sacar(self, valor: float, chave: str | None = None) -> None:
        if not chave:
            chave = self.pede_senha()
        if self.validar_senha(chave):
            if valor <= self.__saldo and valor > 0:
                self.__saldo -= valor
                print(f"Saque de R${valor:,.2f} autorizado na conta {self._id}")
            elif valor == 0:
                print("Nenhum valor foi sacado")
            else:
                print("Valor inválido")
        else:
            print("Senha não confere. Saque não autorizado!")

# Passo 5: Criar método depositar(valor)
    def depositar(self, valor: float) -> None:
        if numero_nao_negativo(valor):
            self.__saldo += valor
            print(f"Depósito de R${valor:,.2f} autorizado na conta {self._id}")
        else:
            print("Valor do depósito inválido")

# Passo 6: Exibir o resultado
print("Criando a conta...")
cc1: ContaBancaria = ContaBancaria(123, "Alex", 1000, "Python")
cc2: ContaBancaria = ContaBancaria(234,"Gustavo", 500, "Gafanhoto")

print("Realizando depósito")
cc1.depositar(500)

print("Realizando saque")
cc1.sacar(200)
cc2.sacar(100)

print("Atualizando o titular da conta")
cc1.nome = "Manoel"

inspect(cc1, private=True, methods=True)
inspect(cc2, private=True, methods=True)
# -| AULA 12 - DOMINE ENCAPSULAMENTO EM PYTHON COM GETTERS, SETTERS E 6 PROJETOS REAIS | DESAFIO 32
