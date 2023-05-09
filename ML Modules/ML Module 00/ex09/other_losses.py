"""You certainly had a lot of fun implementing your loss function. Remember we told you
it was one among many possible ways of measuring the loss. Now, you will get to
implement other metrics. You already know about one of them: MSE. There are several
more which are quite common: RMSE, MAE and R2score.
"""

import numpy as np

def mse_(y, y_hat):
    """
    Description:
    Calculate the MSE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a vector of dimension m * 1.
    y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
    mse: has to be a float.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exceptions.
    """
    if not isinstance(y, np.ndarray) and not isinstance(y_hat, np.ndarray):
        return None
    if y.shape != y_hat.shape:
        return None
    if y.size == 0 or y_hat.size == 0:
        return None
    return (1 / len(y)) * ((y_hat - y).transpose() @ (y_hat - y))


def rmse_(y, y_hat):
    """
    Description:
    Calculate the RMSE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a vector of dimension m * 1.
    y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
    rmse: has to be a float.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exceptions.
    """
    return np.sqrt(mse_(y, y_hat))


def mae_(y, y_hat):
    """
    Description:
    Calculate the MAE between the predicted output and the real output.
    Args:
    y: has to be a numpy.array, a vector of dimension m * 1.
    y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
    mae: has to be a float.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exceptions.
    """
    if not isinstance(y, np.ndarray) and not isinstance(y_hat, np.ndarray):
        return None
    if y.shape != y_hat.shape:
        return None
    if y.size == 0 or y_hat.size == 0:
        return None
    return (1 / len(y)) * np.sum(np.abs(y_hat - y))


def r2score_(y, y_hat):
    """
    Description:
    Calculate the R2score between the predicted output and the output.
    Args:
    y: has to be a numpy.array, a vector of dimension m * 1.
    y_hat: has to be a numpy.array, a vector of dimension m * 1.
    Returns:
    r2score: has to be a float.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exceptions.
    """
    if not isinstance(y, np.ndarray) and not isinstance(y_hat, np.ndarray):
        return None
    if y.shape != y_hat.shape:
        return None
    if y.size == 0 or y_hat.size == 0:
        return None
    return (1 - ((y_hat - y).transpose() @ (y_hat - y)) / \
        ((y - np.mean(y)).transpose() @ (y - np.mean(y))))
