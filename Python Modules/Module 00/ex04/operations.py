"""
- Write a program that takes two integers A and B as arguments and prints the result
of the following operations:
    Sum: A+B
    Difference: A-B
    Product: A*B
    Quotient: A/B
    Remainder: A%B
• If more or less than two argument are provided or if either of the argument is not
an integer, print an error message.
• If no argument are provided, do nothing or print an usage.
• If an operation is impossible, print an error message instead of a numerical result.
"""
if __name__ == "__main__":
    import sys

def simple_calculator(num1: int, num2: int) -> None:
    """
        Simple calculator to do arithmetic operations
    """
    print(f"{'Sum: ':15}", num1 + num2)
    print(f"{'Difference: ':15}", num1 - num2)
    print(f"{'Product: ':15}", num1 * num2)
    if num2 != 0:
        print(f"{'Quotient: ':15}", num1 / num2)
    else:
        print(f"{'Quotient: ':15}", "ERROR (division by zero)")
    if num2 != 0:
        print(f"{'Reminder: ':15}", num1 % num2)
    else:
        print(f"{'Reminder: ':15}", "ERROR (modulo by zero)")
def main() -> None:
    """
        Inorder to simplify the if __name__ == "__main__"
    """
    if len(sys.argv[1:]) == 0:
        print("Usage: python operations.py <number1> <number2>\nExample: python operations.py 10 3")
    elif len(sys.argv[1:]) > 2:
        print(AssertionError("AssertionError: too many arguments"))
    elif len(sys.argv[1:]) == 1:
        print(AssertionError("AssertionError: only one argument provided, required two"))
    else:
        try:
            simple_calculator(int(sys.argv[1]), int(sys.argv[2]))
        except ValueError:
            print(AssertionError("AssertionError: only integers"))

if __name__ == "__main__":
    main()
