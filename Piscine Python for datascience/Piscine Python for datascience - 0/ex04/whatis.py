import sys

# Check if arguments are provided
if len(sys.argv) == 2:
    # Access individual arguments
    arg1 = sys.argv[1]
    try:
        int(arg1)
        if int(arg1) % 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")
    except ValueError:
        print("AssertionError: Argument is not an integer")
elif len(sys.argv) > 2:
    print("AssertionError: More than one argument is provided")
