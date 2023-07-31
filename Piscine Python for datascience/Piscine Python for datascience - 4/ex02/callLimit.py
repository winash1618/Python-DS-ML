from typing import Any, Callable


def callLimit(limit: int):
    """
    Decorator factory to limit the number of
    times a decorated function can be called.

    Args:
        limit (int): The maximum number of
        times the decorated function can be called.

    Returns:
        Callable: The decorator function `callLimiter`
        that applies the call limit to the decorated function.

    Example:
        @callLimit(3)
        def my_function(x):
            return x * 2

        my_function(2)  # Output: 4
        my_function(3)  # Output: 6
        my_function(4)  # Output: 8
        my_function(5)  # Output: Function my_function has
        reached its call limit of 3. It will not be executed.
    """
    count = 0

    def callLimiter(function: Callable) -> Callable:
        """
        Decorator function that limits the number of times
        a decorated function can be called.

        Args:
            function (Callable): The function to be decorated.

        Returns:
            Callable: The decorated function that applies the call limit.

        Note:
            This decorator should be used with functions that
            have no side effects, as the function
            will not be executed when the call limit is reached.
        """
        def limit_function(*args: Any, **kwds: Any) -> Any:
            """
            The decorated function that applies the call limit.

            Args:
                *args: Positional arguments to be passed to the
                original function.
                **kwds: Keyword arguments to be passed to
                the original function.

            Returns:
                Any: The return value of the original function.

            Raises:
                None.

            Note:
                If the call limit is reached, this function will
                not execute the original function
                and will instead print a message indicating the
                call limit has been reached.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                s = (f"Function {function.__name__}"
                     f" has reached its call limit of"
                     f" {limit}. It will not be executed.")
                print(s)
        return limit_function

    return callLimiter
