"""
This program will take a single argument and print whether it is even or odd.
"""
import sys

ArrayList = sys.argv[1:]
if len(ArrayList) == 0:
    raise AssertionError("No argument given")
if len(ArrayList) > 1:
    raise AssertionError("Too many arguments given")
if len(ArrayList) == 1:
    if isinstance(ArrayList[0], str):
        try:
            if int(ArrayList[0]) % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            raise AssertionError("Argument is not a number") from None
    else:
        raise AssertionError("Argument is not a number")
