def exit_message(message: str = None) -> str:
    if(not message):
        message = "Exiting program... Thanks for using it! 😄"
    return message

def display_message_box(text: str = None, sep: str = None, sep_multi: int = None, central: bool = True) -> None:
    if(not text):
        text = "Olá, Mundo!"
    if(not sep):
        sep = "-"
    if(not sep_multi):
        sep_multi = len(text) + 4
    if(central):
        text = "  " + text
    separator: str = sep * sep_multi
    message: str = f"{separator}\n{text}\n{separator}\n"
    print(message)

def yes_no(question: str = "-------\nDo you want to continue? (y/n) ") -> bool:
    while True:
        choice: str = str(input(question))
        if choice not in ("yes", "y", "no", "n"):
            print("-------\nInvalid input! Please enter 'yes'/'y' or 'no'/'n'.")
            continue
        if choice in ("yes", "y"):
            return True
        return False

def error_message(message: str = "ERROR:", color: bool = True) -> None:
    if(color):
        print(f"\033[31m{message}\033[m")
    else:
        print(message)
