"""
vectorized log loss
"""

import numpy as np

def vec_log_loss_(y, y_hat, eps=1e-15):
    """
    Compute the logistic loss value.
    Args:
    y: has to be an numpy.ndarray, a vector of shape m * 1.
    y_hat: has to be an numpy.ndarray, a vector of shape m * 1.
    eps: epsilon (default=1e-15)
    Returns:
    The logistic loss value as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(y, np.ndarray) or \
        not isinstance(y_hat, np.ndarray):
        return None
    if y.size == 0 or y_hat.size == 0:
        return None
    m, n = y.shape
    k, l = y_hat.shape
    if m != k or n != l or n != 1 or l != 1:
        return None
    print((np.ones(y.shape) - y),  np.log(np.ones(y.shape) - y))
    return (-1/m) * (np.dot(y, np.log(y_hat)) + np.dot((np.ones(y.shape) - (y + np.full(y.shape, eps))), np.log(np.ones(y.shape) - (y_hat + np.full(y.shape, eps)))))
