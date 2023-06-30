import sys
from ft_filter import ft_filter

def word_len(word="", count=0) -> bool:
    """
    Return an True if word length is more than count else False
    """
    if len(word) > count:
        return True
    return False

def main() -> None:
    """
        Inorder to simplify the if __name__ == "__main__"
    """
    if len(sys.argv[1:]) == 2:
        try:
            int(sys.argv[1:][1])
        except ValueError:
            print("AssertionError: the arguments are bad")
            exit(0)
        print(ft_filter(word_len, sys.argv[1:][0], int(sys.argv[1:][1])))
    else:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
