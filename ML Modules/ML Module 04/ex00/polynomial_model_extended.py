"""polynomial model extended
"""

import numpy as np

def add_polynomial_features(x, power):
    """Add polynomial features to matrix x by raising its columns to every power in the range of 1 up to the power giveArgs:
    x: has to be an numpy.ndarray, a matrix of shape m * n.
    power: has to be an int, the power up to which the columns of matrix x are going to be raised.
    Returns:
    The matrix of polynomial features as a numpy.ndarray, of shape m * (np), containg the polynomial feature vaNone if x is an empty numpy.ndarray.
    Raises:
    This function should not raise any Exception.
    """
    i = 2
    new_arr = x
    while i <= power:
        new_arr = np.concatenate((new_arr, np.power(x, i)), axis=1)
        i += 1
    return new_arr