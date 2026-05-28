def exit_message(message: str = None) -> str:
    if not message:
        message = "Exiting program... Thanks for using it! 😄"
    return message

def display_message_box(text: str = None, sep: str = None, sep_multi: int = None, central: bool = True) -> None:
    if not text:
        text = "Olá, Mundo!"
    if not sep:
        sep = "-"
    if not sep_multi:
        sep_multi = len(text) + 4
    if central:
        text = "  " + text
    separator: str = sep * sep_multi
    message: str = f"{separator}\n{text}\n{separator}\n"
    print(message)

def yes_no(question: str = None, positive_answer: list[str] = None, negative_answer: list[str] = None, invalid_answer: str = None) -> bool:
    if not question:
        question = "Do you want to continue? (y/n) "
    if not positive_answer:
        positive_answer = ["yes", "y"]
    if not negative_answer:
        negative_answer = ["no", "n"]
    if not invalid_answer:
        invalid_answer = "Invalid input! Please enter 'yes'/'y' or 'no'/'n'."
    while True:
        choice: str = input(question)
        if choice not in (positive_answer[0], positive_answer[1], negative_answer[0], negative_answer[1]):
            error_message(invalid_answer)
            continue
        if choice in positive_answer:
            return True
        return False

def error_message(message: str = None, color: bool = True) -> None:
    if not message:
        message = "ERROR: "
    if color:
        print(f"\033[31m{message}\033[m")
    else:
        print(message)

def sep_rator(sep: str = None, sep_multi: int = None) -> None:
    if not sep:
        sep = "-"
    if not sep_multi:
        sep_multi = 20
    print(f"{sep}" * sep_multi)
