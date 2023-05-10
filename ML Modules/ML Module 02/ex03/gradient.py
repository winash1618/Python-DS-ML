"""
gradient
"""

import numpy as np

def gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.array, without any for-loop.
    The three arrays must have the compatible dimensions.
    Args:
    x: has to be an numpy.array, a matrix of dimension m * n.
    y: has to be an numpy.array, a vector of dimension m * 1.
    theta: has to be an numpy.array, a vector (n +1) * 1.
    Return:
    The gradient as a numpy.array, a vector of dimensions n * 1,
    containg the result of the formula for all j.
    None if x, y, or theta are empty numpy.array.
    None if x, y and theta do not have compatible dimensions.
    None if x, y or theta is not of expected type.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.size == 0 or y.size == 0 or theta.size == 0:
        return None
    if x.ndim != 2 or y.ndim != 2 or theta.ndim != 2 or theta.shape[1] != 1:
        return None
    m, n = x.shape
    if y.shape != (m, 1) or theta.shape != (n+1, 1):
        return None
    X = np.insert(x, 0, np.array([1]), axis=1)
    return (1 / len(y)) * np.dot((X.transpose()) , np.dot(X, theta) - y)
