"""
Understand and manipulate the notion of hypothesis in machine learning. You must
implement a function which adds an extra column of 1's on the left side of a given vector
or matrix
"""

import numpy as np

def add_intercept(x):
    """Adds a column of 1's to the non-empty numpy.array x.
    Args:
    x: has to be a numpy.array of dimension m * n.
    Returns:
    X, a numpy.array of dimension m * (n + 1).
    None if x is not a numpy.array.
    None if x is an empty numpy.array.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray):
        return None
    return np.insert(x, 0, np.array([1]), axis=1)
