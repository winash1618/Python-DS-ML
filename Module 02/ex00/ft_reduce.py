"""
implementing the built-in function map
"""
def ft_reduce(function_to_apply, iterable):
    """
    Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if len(iterable) == 1 or len(iterable) == 0:
        return None
    total = 0
    if isinstance(iterable[0], str):
        total = ''
    for index, element in enumerate(iterable):
        if index == 0:
            total = function_to_apply(element, iterable[index + 1])
        elif not index == 1:
            total = function_to_apply(total, element)
        print(index ,total)
    return total
