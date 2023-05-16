"""
linear loss regression
"""

import numpy as np
from l2_reg import l2

def reg_loss_(y, y_hat, theta, lambda_):
    """Computes the regularized loss of a linear regression model from two non-empty numpy.array, without any for loop.Args:
    y: has to be an numpy.ndarray, a vector of shape m * 1.
    y_hat: has to be an numpy.ndarray, a vector of shape m * 1.
    theta: has to be a numpy.ndarray, a vector of shape n * 1.
    lambda_: has to be a float.
    Returns:
    The regularized loss as a float.
    None if y, y_hat, or theta are empty numpy.ndarray.
    None if y and y_hat do not share the same shapes.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if not isinstance(lambda_, float):
        return None
    if y.size is 0 or y_hat.size is 0 or theta.size is 0:
        return None
    if y.shape != y_hat.shape:
        return None
    m, _ = y.shape
    return ((1 / (2 * m)) * (np.dot((y_hat - y).transpose(), y_hat - y) + lambda_ * l2(theta))).item()
