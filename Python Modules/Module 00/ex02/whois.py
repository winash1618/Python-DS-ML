"""
This program will take a single argument and print whether it is even or odd.
"""
import sys

ArrayList = sys.argv[1:]
if len(ArrayList) == 0:
    print("Usage: python whois.py <number>")
if len(ArrayList) > 1:
    print("AssertionError: more than one argument are provided")
if len(ArrayList) == 1:
    if isinstance(ArrayList[0], str):
        try:
            if int(ArrayList[0]) % 2 == 0:
                if int(ArrayList[0]) == 0:
                    print("I'm Zero.")
                else:
                    print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            print("AssertionError: Argument is not an integer")
    else:
        print("AssertionError: Argument is not an integer")
