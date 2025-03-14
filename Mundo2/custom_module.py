# Dictionaries containing ANSI codes for styles, text colors, and background
STYLE: dict[str, str] = {
    'none': '0',  # No style
    'bd':'1',     # Bold
    'u':'4',      # Underline
    'n':'7'       # Negative (inverts colors)
}
COLOR: dict[str, str] = {
    'none': '0', 'gy': '30', 'r': '31', 'g': '32',
    'y': '33', 'b': '34', 'p': '35', 'c': '36', 'w': '37'
}
BACKGROUND: dict[str, str] = {
    'none': '0', 'gy': '40', 'r': '41', 'g': '42',
    'y': '43', 'b': '44', 'p': '45', 'c': '46', 'w': '47'
}


def txt_style(
    txt: str,
    style_: str | None = None,
    color_: str | None = None,
    background_: str | None = None
) -> str:
    """
    Applies ANSI styles and colors to the given text.

    Args:
        txt (str): The text to be formatted.
        style_ (str | None, optional): Text style. Options:
            - 'none' (default)
            - 'bd' (bold)
            - 'u' (underline)
            - 'n' (negative/inverted)
        color_ (str | None, optional): Text color. Options:
            - 'none' (default), 'gy' (gray), 'r' (red), 'g' (green), 'y' (yellow)
            - 'b' (blue), 'p' (purple), 'c' (cyan), 'w' (white)
        background_ (str | None, optional): Background color. Same options as `color_`.

    Returns:
        str: The formatted text with ANSI escape codes.
    """
    codes: list[str] = []

    if style_ and style_ != 'none':
        codes.append(STYLE.get(style_, '0'))
    if color_ and color_ != 'none':
        codes.append(COLOR.get(color_, '0'))
    if background_ and background_ != 'none':
        codes.append(BACKGROUND.get(background_, '0'))

    return f"\033[{';'.join(codes)}m{txt}\033[m"


def sepa_rator(length: int | None = None, color: str | None = None) -> str:
    """
    _summary_

    Args:
        length (int | None, optional): _description_. Defaults to None.
        color (str | None, optional): _description_. Defaults to None.

    Returns:
        str: _description_
    """
    if length is None:
        length = 21

    if color is None:
        color = None

    return txt_style("-=-", color_ = color) * length


def error_message(message: str = "Please enter a valid option.") -> str:
    """
    _summary_

    Args:
        message (str, optional): _description_. Defaults to "Please enter a valid option.".

    Returns:
        str: _description_
    """
    return txt_style(message, 'bd', 'r')


def print_error(lenght: int | None = None) -> None:
    """Print a formatted error message."""
    print(sepa_rator(lenght, 'c'))
    print(error_message())
    print(sepa_rator(lenght, 'c'))


if __name__ == "__main__":
    print(txt_style("Hello, World!", 'u', 'r', 'b'))
    print(sepa_rator())
    print(error_message())
