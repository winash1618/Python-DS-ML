"""
test file
"""
from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce

# Example 1:
x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))
# Output:
# <generator object ft_map at 0x7f708faab7b0> # The address will be different
print(list(ft_map(lambda t: t + 1, x)))
# Output:
# [2, 3, 4, 5, 6]

# Example 2:
print(ft_filter(lambda dum: not (dum % 2), x))
# Output:
# <generator object ft_filter at 0x7f709c777d00> # The address will be different
print(list(ft_filter(lambda dum: not (dum % 2), x)))
# Output:
# [2, 4]

# Example 3:
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
# Output:
# "Hello world"
ft_reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])

def test_ft_reduce():
    """
    ft_reduce tester
    """
    assert ft_reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]) == 15
    assert ft_reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]) == 120
    assert ft_reduce(lambda x, y: x + y, ["Hello", " ", "world"]) == "Hello world"
    print( ft_reduce(lambda x, y: x if len(x) > len(y) else y, ["apple", "banana", "cherry", "durian"]))
    assert ft_reduce(lambda x, y: x if x < y else y, [4, 1, 3, 5, 2]) == 1
    assert ft_reduce(lambda x, y: x if x > y else y, [4, 1, 3, 5, 2]) == 5
    assert ft_reduce(lambda x, y: x + y, []) is None

test_ft_reduce()
