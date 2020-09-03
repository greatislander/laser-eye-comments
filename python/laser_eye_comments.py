import re


def convert_to_morse_code(str: str):
    """Converts a string to Morse Code.

    Parameters
    ----------
    str : str
        The string to be converted to Morse Code.
    
    Returns
    -------
    str
        The string as Morse Code.
    """
    morse_code_dictionary = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
    }

    # Change letters to lowercase.
    str = str.lower()

    # Strip all characters except numbers, letters, and spaces.
    # TODO: This needs to be tested with accented characters.
    str = re.sub('[^0-9a-z ]', '', str)

    # For each character in the Morse Code dictionary, replace all occurences
    # in the string with their Morse Code equivalent.
    for item in morse_code_dictionary.keys():
        str = re.sub(item, morse_code_dictionary[item], str)

    # Return the converted string.
    return str
