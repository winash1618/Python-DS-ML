"""
gradient descent
"""

import numpy as np
from prediction import predict_

def simple_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.array, with a for-loop.
    The three arrays must have compatible shapes.
    Args:
    x: has to be an numpy.array, a vector of shape m * 1.
    y: has to be an numpy.array, a vector of shape m * 1.
    theta: has to be an numpy.array, a 2 * 1 vector.
    Return:
    The gradient as a numpy.array, a vector of shape 2 * 1.
    None if x, y, or theta are empty numpy.array.
    None if x, y and theta do not have compatible shapes.
    None if x, y or theta is not of the expected type.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.shape != y.shape or len(theta) != 2:
        return None
    if x.size == 0 or y.size == 0 or theta.size == 0:
        return None
    y_hat = predict_(x, theta)
    j1 = [np.mean(y_hat - y)]
    j2 = [np.mean((y_hat - y) * x)]
    return np.array([j1, j2])
