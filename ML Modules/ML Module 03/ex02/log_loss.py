"""
Logarithmic Loss
"""

import numpy as np
import math

def log_loss_(y, y_hat, eps=1e-15):
    """
    Computes the logistic loss value.
    Args:
    y: has to be an numpy.ndarray, a vector of shape m * 1.
    y_hat: has to be an numpy.ndarray, a vector of shape m * 1.
    eps: has to be a float, epsilon (default=1e-15)
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
    i = 0
    total = 0
    while i < m:
        y_i = y[i, 0]
        y_hat_i = y_hat[i, 0]
        total += y_i * math.log(y_hat_i + eps) + (1 - y_i) * math.log(1 - (y_hat_i + eps))
        i += 1
    return (-1/m) * total
