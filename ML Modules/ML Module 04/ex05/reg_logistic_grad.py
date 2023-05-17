
import numpy as np

def reg_logistic_grad(y, x, theta, lambda_):
    """Computes the regularized logistic gradient of three non-empty numpy.ndarray, with two for-loops. The three arrayArgs:
    y: has to be a numpy.ndarray, a vector of shape m * 1.
    x: has to be a numpy.ndarray, a matrix of dimesion m * n.
    theta: has to be a numpy.ndarray, a vector of shape n * 1.
    lambda_: has to be a float.
    Returns:
    A numpy.ndarray, a vector of shape n * 1, containing the results of the formula for all j.
    None if y, x, or theta are empty numpy.ndarray.
    None if y, x or theta does not share compatibles shapes.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(y, np.ndarray) or not isinstance(x, np.ndarray) \
        or not isinstance(theta, np.ndarray) or not isinstance(lambda_, float):
        return None
    if y.size is 0 or x.size is 0 or theta.size is 0:
        return None
    m, n = x.shape
    l, p = y.shape
    k, j = theta.shape
    if m != l or k != n + 1 or p != j or p != 1:
        return None
    print(m, n, l, p, k, j)
    X = np.insert(x, 0, np.array([1]), axis=1)
    j = 0
    grad = np.zeros(theta.shape)
    theta_ = np.array(theta)
    theta_[0] = 0
    while j <= n:
        i = 0
        tot = 0
        if j is 0:
            while i < m:
                tot += (1 / (1 + np.exp(-np.dot(X[i,:].reshape(-1, 1).transpose(), theta)))) - y[i]
                i += 1
            tot = (1/m) * tot
        else:
            while i < m:
                tot += (((1 / (1 + np.exp(-np.dot(X[i,:].reshape(-1, 1).transpose(), theta)))) - y[i]) * X[i][j])
                i += 1
            tot = (1/m) * (tot + lambda_ * theta_[j])
        grad[j] = np.array(tot.item())
        j += 1
    return (grad)
def vec_reg_logistic_grad(y, x, theta, lambda_):
    """Computes the regularized logistic gradient of three non-empty numpy.ndarray, without any for-loop. The three arrArgs:
    y: has to be a numpy.ndarray, a vector of shape m * 1.
    x: has to be a numpy.ndarray, a matrix of shape m * n.
    theta: has to be a numpy.ndarray, a vector of shape n * 1.
    lambda_: has to be a float.
    Returns:
    A numpy.ndarray, a vector of shape n * 1, containing the results of the formula for all j.
    None if y, x, or theta are empty numpy.ndarray.
    None if y, x or theta does not share compatibles shapes.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(y, np.ndarray) or not isinstance(x, np.ndarray) \
        or not isinstance(theta, np.ndarray) or not isinstance(lambda_, float):
        return None
    if y.size is 0 or x.size is 0 or theta.size is 0:
        return None
    m, n = x.shape
    l, p = y.shape
    k, j = theta.shape
    if m != l or k != n + 1 or p != j or p != 1:
        return None
    X = np.insert(x, 0, np.array([1]), axis=1)
    theta_ = np.array(theta)
    theta_[0] = 0
    return (1 / m) * (np.dot(X.transpose(), (1 / (1 + np.exp(-np.dot(X, theta))) - y)) + (lambda_ * theta_))
    