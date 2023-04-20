"""
Make a program that takes a string S and an integer N as argument and print the list
of words in S that contains more than N non-punctuation characters.
    • Words are separated from each other by space characters
    • Punctuation symbols must be removed from the printed list: they are neither 
        part of a word nor a separator
    • The program must contains at least one list comprehension expression.
If the number of argument is different from 2, or if the type of any argument is wrong,
the program prints an error message.
"""
import string

if __name__ == "__main__":
    import sys

def list_words(S: str, N: int) -> None:
    """
    print the list of words in S that contains more than N non-punctuation characters
    """
    words = S.split()
    for word in words:
        count = 0
        for character in word:
            if character not in string.punctuation:
                count += 1
        if count <= N:
            words.remove(word)
    print(words)

def main() -> None:
    """
        Inorder to simplify the if __name__ == "__main__"
    """
    if len(sys.argv[1:]) == 2:
        try:
            int(sys.argv[1:][1])
        except ValueError:
            print("Error")
            exit(0)
        list_words(sys.argv[1:][0], int(sys.argv[1:][1]))
    else:
        print("Error")

if __name__ == "__main__":
    main()
