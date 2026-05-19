def text_color(text: str, color: str) -> str:
    colors: dict[str, str] = {"vermelho": "\033[31m", "verde": "\033[32m",
                              "amarelo": "\033[33m", "azul": "\033[34m"}
    text = f"{colors[color]}{text}\033[m"
    return text
