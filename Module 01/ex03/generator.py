"""
The goal of the exercise is to discover the concept of generator object in Python
Code a function called generator that takes a text as input (only printable characters), uses the string parameter sep as a splitting parameter, and yields the resulting
substrings.
The function can take an optional argument. The options are:
	• shuffle: shuffles the list of words,
	• unique: returns a list where each word appears only once,
	• ordered: alphabetically sorts the words.
"""

import random

def generator(text, sep=" ", option=None):
    """
    Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    """
    # try:
    if not isinstance(text, str):
        print("ERROR")
        exit(0)
    lst = text.split(sep)
    if option == "shuffle":
        print("shuffle")
        for i, element in enumerate(lst):
            j = random.randint(0, i)
            temp = element
            lst[i] = lst[j]
            lst[j] = temp
        return lst
    elif option == "unique":
        print("unique")
        lst = list(set(lst))
        return lst
    elif option == "ordered":
        print("ordered")
        lst.sort()
        return lst
    elif not None and not isinstance(option, str):
        print("ERROR")
        exit(0)
    return lst
