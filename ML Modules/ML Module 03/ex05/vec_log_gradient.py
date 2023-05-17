"""
Vectorized Logistic regression
"""

import numpy as np

def vec_log_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.ndarray, without any for-loop. The three arrays must have compArgs:
    x: has to be an numpy.ndarray, a matrix of shape m * n.
    y: has to be an numpy.ndarray, a vector of shape m * 1.
    theta: has to be an numpy.ndarray, a vector (n +1) * 1.
    Returns:
    The gradient as a numpy.ndarray, a vector of shape n * 1, containg the result of the formula for all j.
    None if x, y, or theta are empty numpy.ndarray.
    None if x, y and theta do not have compatible shapes.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.size == 0 or y.size == 0 or theta.size == 0:
        return None
    m, n = x.shape
    l, k = y.shape
    o, p = theta.shape
    if m != l or k != 1 or p != 1 or o != n + 1:
        return None
    X = np.insert(x, 0, np.array([1]), axis=1)
    y_hat = 1 / (1 + np.exp(-np.ones(y.shape) * np.dot(X, theta)))
    return (1 / m) * np.dot(X.transpose(), y_hat - y).squeeze()
