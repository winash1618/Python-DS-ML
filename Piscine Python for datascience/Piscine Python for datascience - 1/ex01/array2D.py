from typing import List


def slice_me(family: List[List], start: int, end: int) -> List[List]:
    """Slice a list of lists (2D list) from the specified
    start index to the end index.

    Args:
        family (List[List]): The 2D list to be sliced.
        start (int): The starting index of the slice (inclusive).
        end (int): The ending index of the slice (exclusive).

    Returns:
        List[List]: The sliced 2D list.
    """
    shape = len(family), len(family[0])
    print(f"My shape is: {shape}")
    new_family = family[start:end]
    shape = (len(new_family), len(new_family[0]))
    print(f"My new shape is: {shape}")
    return new_family
