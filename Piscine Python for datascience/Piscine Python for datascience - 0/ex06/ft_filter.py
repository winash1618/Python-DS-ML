def ft_filter(func=None, my_string="", count=None) -> list:
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item)is true.
    If function is None, return the items that are true.
    """
    return [word for word in my_string.split() if func(word, count)]
