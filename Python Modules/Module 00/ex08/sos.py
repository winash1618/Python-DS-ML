"""
Make a program that takes a string as argument and encode it into Morse code.
    • The program supports space and alphanumeric characters
    • An alphanumeric character is represented by dots . and dashes -:
    • A space character is represented by a slash /
    • Complete morse characters are separated by a single space
If more than one argument are provided, merge them into a single string with each
argument separated by a space character.
If no argument is provided, do nothing or print an usage.
"""

if __name__ == "__main__":
    import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ': '/'}

def string_to_morse_code_converter(my_string: str):
    """
    takes a string as argument and encode it into Morse code.
    """
    try:
        morse_code = [MORSE_CODE_DICT[char] for char in my_string.upper()
                      if len(MORSE_CODE_DICT[char]) > 0]
    except KeyError:
        print("ERROR")
        exit(0)
    for code in morse_code:
        print(code, end=' ')
    print('')

def main() -> None:
    """
        Inorder to simplify the if __name__ == "__main__"
    """
    if len(sys.argv[1:]) >= 1:
        string_to_morse_code_converter(' '.join(sys.argv[1:]))

if __name__ == "__main__":
    main()
