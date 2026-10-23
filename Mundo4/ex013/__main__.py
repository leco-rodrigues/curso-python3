from classes import *


def main():
    p1: Mae = Mae("Jaciara")
    p2: Filho = Filho("Matheus")
    p3: Filha = Filha("Mônica")

    p1.fazer_pudim()
    p1.fritar_coxinha()

    p2.fazer_pudim()
    p2.fritar_coxinha()

    p3.fazer_pudim()
    p3.fritar_coxinha()

if __name__ == "__main__":
    main()
