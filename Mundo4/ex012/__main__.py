from classes import *


def main():
    a: Cachorro = Cachorro("Bandit")
    b: Gato = Gato("Frajola")
    c: Pato = Pato("Donald")
    d: Galinha = Galinha("Pintadinha")
    e: Spitz = Spitz("Luluzinha")
    f: PitBull = PitBull("Guerreiro")

    a.emitir_som()
    b.emitir_som()
    c.emitir_som()
    d.emitir_som()

if __name__ == "__main__":
    main()
