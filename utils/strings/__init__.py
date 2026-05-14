def exit_message(message: str = None) -> str:
    if(not message):
        message = "Exiting program... Thanks for using it! 😄"
    return message

def display_message_box(text: str = None, sep: str = None, sep_multi: int = None, central: bool = True) -> None:
    if(not text):
        text = "Olá, Mundo!"
    if(not sep):
        sep = "~"
    if(not sep_multi):
        sep_multi = len(text) + 4
    if(central):
        text = "  " + text
    separator: str = sep * sep_multi
    message: str = f"\n{separator}\n{text}\n{separator}\n"
    print(message)
