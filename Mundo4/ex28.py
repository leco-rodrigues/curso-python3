# Termostato Inteligente:
    # Implemente um termostato orientado a objetos.
        # classe Termostato
        # Mínimo 16°C, máximo 30°C, inicia em 24°C, incremento 0.5°C
        # __temperatura
        # @temperatura
        # @ftemperatura

# Passo 1: Criar classe Termostato
class Termostato:
    MIN: float = 16.0
    MAX: float = 30.0
    INCREMENTO: float = 0.5

    def __init__(self, temperatura: float = 24.0) -> None:
        self.__temperatura = temperatura

    @property
    def temperatura(self) -> float:
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor: float) -> None:
        if valor % Termostato.INCREMENTO == 0:
            if Termostato.MIN <= valor <= Termostato.MAX:
                self.__temperatura = valor
            elif Termostato.MIN > valor:
                self.__temperatura = Termostato.MIN
            elif Termostato.MAX < valor:
                self.__temperatura = Termostato.MAX
        else:
            print(f"Temperatura de {valor}°C é inválida!")

    @property
    def ftemperatura(self) -> str:
        return f"{self.__temperatura}°C"

# Passo 2: Exibir o resultado
t: Termostato = Termostato()
t.temperatura = 30

print(f"A temperatura atual é de {t.ftemperatura}")
# -| AULA 12 - DOMINE ENCAPSULAMENTO EM PYTHON COM GETTERS, SETTERS E 6 PROJETOS REAIS | DESAFIO 28
