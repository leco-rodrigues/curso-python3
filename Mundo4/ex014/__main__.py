from classes import *


def main():
    x: Analisador = Analisador()

    x.analisar(85)
    x.analisar(8.5)
    x.analisar("8.5")
    x.analisar((3, 5, 7))
    x.analisar([3, '5', 7])
    x.analisar({"nome": "Alex", "idade": 27})
    x.analisar(None)
    x.analisar(len([6, 9, 2]))
    x.analisar(max([6, 9.3, 2]))

if __name__ == "__main__":
    main()
