"""
test
"""
import numpy as np

def log_gradient(x, y, theta):
    """Computes a gradient vector from three non-empty numpy.ndarray, with a for-loop. The three arrays must have compatiblArgs:
    x: has to be an numpy.ndarray, a matrix of shape m * n.
    y: has to be an numpy.ndarray, a vector of shape m * 1.
    theta: has to be an numpy.ndarray, a vector of shape (n + 1) * 1.
    Returns:
    The gradient as a numpy.ndarray, a vector of shape n * 1, containing the result of the formula for all j.
    None if x, y, or theta are empty numpy.ndarray.
    None if x, y and theta do not have compatible dimensions.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray) or not isinstance(theta, np.ndarray):
        return None
    if x.size == 0 or y.size == 0 or theta.size == 0:
        return None
    m, n = x.shape
    k, l = y.shape
    p, q = theta.shape
    if m != k or l != 1 or n != p - 1 or q != 1:
        return None
    j = 0
    nabla = np.zeros(n + 1)
    X = np.insert(x, 0, np.array([1]), axis=1)
    while j <= n:
        i = 0
        tot = 0
        while i < m:
            if i == 0:
                y_hat = 1 / (1 + np.exp(-1 * np.dot(theta.transpose(), X[i, :].reshape(-1, 1))))
                tot += y_hat.squeeze() - y[i].squeeze()
            else:
                y_hat = 1 / (1 + np.exp(-1 * np.dot(theta.transpose(), X[i, :].reshape(-1, 1))))
                tot += (y_hat.squeeze() - y[i].squeeze()) * X[i][j]
            i += 1
        nabla[j] = tot / m
        j += 1
    return nabla
