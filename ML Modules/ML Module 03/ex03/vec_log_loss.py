"""
vectorized log loss
"""

import numpy as np

def value_corrector(x, eps=1e-15):
    """To avoid log error

    Args:
        x (float): value to converted
        eps (decimal, optional): value to add. Defaults to 1e-15.

    Returns:
        double: converted value
    """
    if int(x) == 0 or int(x) == 1:
        if x >= 1 - eps:
            return x - eps
        elif x <= eps:
            return x + eps
    return x

def vec_log_loss_(y, y_hat, eps=1e-8):
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
    # y_hat =  np.array([[0.99930437], [0], [1]])
    # y_hatsafe = y_hat + epsm
    # y_hat_safe = np.clip(y_hat, eps, 1 - eps)
    vec_func = np.vectorize(value_corrector)
    y_hatsafe = vec_func(y_hat)
    # print(y_hatsafe)
    loss = (-1/m) * (np.dot(y.transpose(), np.log(y_hatsafe)) \
                     + np.dot(1 - y.transpose(), np.log(1 - y_hatsafe)))
    return loss.item()
