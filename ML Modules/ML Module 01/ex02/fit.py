"""Understand and manipulate the notion of gradient and gradient descent in machine learning. Be able to explain what it means to fit a Machine Learning model to a dataset.
Implement a function that performs Linear Gradient Descent (LGD).
    """

from vec_gradient import simple_gradient

def fit_(x, y, theta, alpha, max_iter):
    """
    Description:
    Fits the model to the training dataset contained in x and y.
    Args:
    x: has to be a numpy.ndarray, a vector of dimension m * 1: (number of training examples, 1).
    y: has to be a numpy.ndarray, a vector of dimension m * 1: (number of training examples, 1).
    theta: has to be a numpy.ndarray, a vector of dimension 2 * 1.
    alpha: has to be a float, the learning rate
    max_iter: has to be an int, the number of iterations done during the gradient descent
    Returns:
    new_theta: numpy.ndarray, a vector of dimension 2 * 1.
    None if there is a matching dimension problem.
    Raises:
    This function should not raise any Exception.
    """
    i = 0
    while i < max_iter:
        j = simple_gradient(x, y, theta)
        theta = theta - alpha * j
        i += 1
    return theta
