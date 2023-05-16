"""
logistic loss regression
"""
import numpy as np
from l2_reg import l2

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

def reg_log_loss_(y, y_hat, theta, lambda_):
    """Computes the regularized loss of a logistic regression model from two non-empty numpy.ndarray, without any for lArgs:
    y: has to be an numpy.ndarray, a vector of shape m * 1.
    y_hat: has to be an numpy.ndarray, a vector of shape m * 1.
    theta: has to be a numpy.ndarray, a vector of shape n * 1.
    lambda_: has to be a float.
    Returns:
    The regularized loss as a float.
    None if y, y_hat, or theta is empty numpy.ndarray.
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
    vec_func = np.vectorize(value_corrector)
    y_hatsafe = vec_func(y_hat)
    return ((-1/m) * (np.dot(y.transpose(), np.log(y_hat)) + np.dot((1 - y).transpose(), np.log(1 - y_hatsafe))) + (lambda_ / (2 * m)) * l2(theta)).item()
