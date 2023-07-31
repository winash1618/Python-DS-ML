def square(x: int | float) -> int | float:
    """
    Calculate the square of a given number.

    Args:
        x (int | float): The input number.

    Returns:
        int | float: The square of the input number.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Calculate the power of a number to itself.

    Args:
        x (int | float): The input number.

    Returns:
        int | float: The power of the input number to itself.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Generate and return a closure function that applies the given
    function repeatedly to the input.

    Args:
        x (int | float): The initial input number.
        function: The function to be applied to the input number.

    Returns:
        object: A closure function that repeatedly applies the given
        function to the input number.

    Example:
        square_outer = outer(2, square)
        result = square_outer()  # 2^2 = 4
        result = square_outer()  # 4^2 = 16
        result = square_outer()  # 16^2 = 256
    """
    count = 0

    def inner() -> float:
        """
        The closure function that applies the given function repeatedly
        to the input.

        Returns:
            float: The result after applying the function repeatedly.
        """
        i = 0
        nonlocal count
        result = x
        count += 1
        for i in range(count):
            result = function(result)
            i += 1
        return result

    return inner
