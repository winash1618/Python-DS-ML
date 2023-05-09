"""
Understand and manipulate the notion of loss function in machine learning.
"""

import numpy as np

def loss_(y, y_hat):
    """Computes the half mean squared error of two non-empty numpy.array, without any for loop.
    The two arrays must have the same dimensions.
    Args:
    y: has to be an numpy.array, a vector.
    y_hat: has to be an numpy.array, a vector.
    Returns:
    The half mean squared error of the two vectors as a float.
    None if y or y_hat are empty numpy.array.
    None if y and y_hat does not share the same dimensions.
    Raises:
    This function should not raise any Exceptions.
    """
    if not isinstance(y, np.ndarray) and not isinstance(y_hat, np.ndarray):
        return None
    if y.shape != y_hat.shape:
        return None
    if y.size == 0 or y_hat.size == 0:
        return None
    return (1 / (2 * len(y))) *( (y_hat - y).transpose() @ (y_hat - y))
