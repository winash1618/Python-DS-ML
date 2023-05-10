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
    if isinstance(x, np.ndarray):
        if x.ndim == 1:
            if x.size != 0:
                new_x = np.array([[i] for i in x])
                one = np.array([1])
                return np.insert(new_x, 0, one, axis = 1)
        else:
            if x.size != 0:
                return (np.insert(x, 0, np.full((x.shape[0],), 1), axis = 1))
