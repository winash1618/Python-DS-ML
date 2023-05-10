"""
prediction
"""

import numpy as np

def predict_(x, theta):
    """Computes the prediction vector y_hat from two non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of dimensions m * n.
    theta: has to be an numpy.array, a vector of dimensions (n + 1) * 1.
    Return:
    y_hat as a numpy.array, a vector of dimensions m * 1.
    None if x or theta are empty numpy.array.
    None if x or theta dimensions are not appropriate.
    None if x or theta is not of expected type.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.size == 0 or theta.size == 0:
        return None
    return np.dot(np.insert(x, 0, np.array([1]), axis=1), theta)