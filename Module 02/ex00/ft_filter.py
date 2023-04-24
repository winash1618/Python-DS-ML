"""
implementing the filter in built-in function
"""
def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    new_iterable = []
    for element in iterable:
        if function_to_apply(element):
            new_iterable.append(element)
    return new_iterable