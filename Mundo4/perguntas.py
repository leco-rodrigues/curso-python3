from utils.strings import display_message_box, sep_rator, error_message, yes_no
from utils.colors import text_color

def pergunta(perg: str, a: str, b: str, c: str, d: str, resp: str) -> None:
    while True:
        display_message_box(text_color(perg, "azul"), sep_multi = 60)

        print(text_color("A", "amarelo") + " - " + text_color(a, "azul"))
        print(text_color("B", "amarelo") + " - " + text_color(b, "azul"))
        print(text_color("C", "amarelo") + " - " + text_color(c, "azul"))
        print(text_color("D", "amarelo") + " - " + text_color(d, "azul"))

        try:
            resposta: str = input(text_color("\nQual a alternativa correta?\n", "azul"))
        
            if resposta.strip().upper() not in ("A", "B", "C", "D"):
                sep_rator(sep_multi = 60)
                error_message("ERRO: Por favor, escolha uma alternativa válida.")
                continue
            if resposta.upper() == resp:
                sep_rator(sep_multi = 60)
                print(text_color("Alternativa correta!", "verde"))
                break
                        
            sep_rator(sep_multi = 60)
            error_message("Alternativa incorreta!")
            sep_rator(sep_multi = 60)

            if not yes_no(text_color("Você quer continuar? (s/n) ", "azul"), ["sim", "s"], ["não", "n"], "ERRO: Por favor, digite 'sim'/'s' ou 'não','n'"):
                break
        except KeyboardInterrupt:
            sep_rator(sep_multi = 60)
            error_message("O usuário decidiu interromper a execução do programa.")
            break
