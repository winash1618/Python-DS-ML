"""
logistic predict
"""

import numpy as np

def logistic_predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * n.
    theta: has to be an numpy.ndarray, a vector of dimension (n + 1) * 1.
    Returns:
    y_hat as a numpy.ndarray, a vector of dimension m * 1.
    None if x or theta are empty numpy.ndarray.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.size == 0 or theta.size == 0:
        return None
    m, n = x.shape
    k, l = theta.shape
    if n != k - 1 or l != 1:
        return None
    X = np.insert(x, 0, np.array([1]), axis=1)
    return (1 / (1 + np.exp(np.dot(-X, theta))))
