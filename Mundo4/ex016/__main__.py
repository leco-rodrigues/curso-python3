from classes import *


def main():
    a: Porta = Porta()
    b: Empresa = Empresa()
    c: Ovo = Ovo()
    d: Pedra = Pedra()

    """
    a.abrir()
    b.abrir()
    c.abrir()
    d.abrir()
    """

    tentar_abrir(a)
    tentar_abrir(b)
    tentar_abrir(c)
    tentar_abrir(d)

if __name__ == "__main__":
    main()
