"""
implementing the built-in function map
"""
def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    new_iterable = []
    for element in iterable:
        new_iterable.append(function_to_apply(element))
    return new_iterable