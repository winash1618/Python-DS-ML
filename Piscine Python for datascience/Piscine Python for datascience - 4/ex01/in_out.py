def square(x: int | float) -> int | float:
    return x * x
def pow(x: int | float) -> int | float:
    return x ** x
def outer(x: int | float, function) -> object:
    count = 0
    def inner() -> float:
        i = 0
        nonlocal count
        result = x
        count += 1
        for i in range(count):
            result = function(result)
            i += 1
        return result
    return inner