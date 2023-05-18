"""
l2 regression
"""

import numpy as np

def iterative_l2(theta):
    """Computes the L2 regularization of a non-empty numpy.ndarray, with a for-loop.
    Args:
    theta: has to be a numpy.ndarray, a vector of shape n * 1.
    Returns:
    The L2 regularization as a float.
    None if theta in an empty numpy.ndarray.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(theta, np.ndarray):
        return None
    if theta.size == 0:
        return None
    i = 1
    tot = 0
    while i < theta.size:
        tot += theta[i] * theta[i]
        i += 1
    return tot.item()

def l2(theta):
    """Computes the L2 regularization of a non-empty numpy.ndarray, without any for-loop.
    Args:
    theta: has to be a numpy.ndarray, a vector of shape n * 1.
    Returns:
    The L2 regularization as a float.
    None if theta in an empty numpy.ndarray.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(theta, np.ndarray):
        return None
    if theta.size == 0:
        return None
    theta[0] = 0
    return (theta.transpose() @ theta).item()
