from typing import Any, Callable

def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Function {function.__name__} has reached its call limit of {limit}. It will not be executed.")
        return limit_function

    return callLimiter
