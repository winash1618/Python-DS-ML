"""_summary_
    """

import numpy as np

def simple_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.array, without any for loop.
    The three arrays must have compatible shapes.
    Args:
    x: has to be a numpy.array, a matrix of shape m * 1.
    y: has to be a numpy.array, a vector of shape m * 1.
    theta: has to be a numpy.array, a 2 * 1 vector.
    Return:
    The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
    None if x, y, or theta is an empty numpy.ndarray.
    None if x, y and theta do not have compatible dimensions.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray)\
        or not isinstance(theta, np.ndarray):
        return None
    if x.shape != y.shape or len(theta) != 2:
        return None
    if x.size == 0 or y.size == 0 or theta.size == 0:
        return None
    x_hat = np.insert(x, 0, np.array([1]), axis=1)
    return (1/(len(y))) * x_hat.transpose() @ (x_hat @ theta - y)
