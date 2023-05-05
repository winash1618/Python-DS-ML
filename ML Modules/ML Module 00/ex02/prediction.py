"""
Prediction:Understand and manipulate the notion of hypothesis in machine learning
"""

import numpy as np


def simple_predict(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.ndarray, a vector of dimension m * 1.
    None if x or theta are empty numpy.ndarray.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exception.
    """
    if isinstance(x, np.ndarray) and isinstance(theta, np.ndarray) \
        and theta.size == 2 and x.size != 0:
        return theta[0] + x * theta[1]
