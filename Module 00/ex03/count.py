"""
Program that counts the number of characters in a String.
language: python3
important note: when you import the function to the terminal python3 environment and
if you change anything inside the code you need to import it again. otherwise you won't
have those changes.
links: https://realpython.com/if-name-main-python/
"""
import string
if __name__ == "__main__":
    import sys

def text_analyzer(_string = "") -> None:
    """
        This function counts the number of upper characters, 
        lower characters, punctuation and spaces in a given text.
    """
    if not isinstance(_string, str):
        raise AssertionError("argument is not a string")
    while len(_string) == 0:
        _string = input("What is the text to analyze?")
    counter = [0] * 4
    for character in _string:
        if character.isspace():
            counter[0] += 1
        elif character.isupper():
            counter[1] += 1
        elif character.islower():
            counter[2] += 1
        elif character in string.punctuation:
            counter[3] += 1
    print("The text contains", len(_string), "character(s): ")
    print("- ", counter[1], " upper letter(s)")
    print("- ", counter[2], " lower letter(s)")
    print("- ", counter[3], " punctuation mark(s)")
    print("- ", counter[0], " space(s)")

def main() -> None:
    """
        This function is made to shorten the length of __name__ == "__main__" condition
    """
    if len(sys.argv[1:]) == 1:
        text_analyzer(sys.argv[1])
    else:
        raise AssertionError("input error, multiple arguements provided")

if __name__ == "__main__":
    main()
