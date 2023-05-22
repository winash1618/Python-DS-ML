"""
Write a class that contains all methods necessary to perform linear regression.
"""

import numpy as np

class MyLinearRegression():
    """
    Description:
    My personnal linear regression class to fit like a boss.
    """

    def __init__(self, thetas, alpha=0.00000001, max_iter=6000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas

    def fit_(self, x, y):
        """Fits the model to the training dataset contained in x and y.

        Args:
            x (numpy.ndarray): a vector of dimension m * 1
            y (numpy.ndarray): a vector of dimension m * 1
        """
        if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
            return None
        if x.size == 0 or y.size == 0:
            return None
        m, n = x.shape
        l, k = y.reshape(-1, 1).shape
        if m != l:
            return None
        i = 0
        X = np.insert(x, 0, np.array([1]), axis=1)
        print(X.shape, self.thetas.shape, y.shape)
        while i < self.max_iter:
            grad = (1 / len(y)) * np.dot((X.transpose()) , np.dot(X, self.thetas) - y)
            self.thetas = self.thetas - self.alpha * grad
            i += 1
        return self.thetas

    def mse_(self, y_hat, y):
        """_summary_

        Args:
            y (numpy.ndarray): a vector of dimension m * 1
            y_hat (numpy.ndarray): a vector of dimension m * 1
        """
        return np.dot((y - y_hat).transpose(), (y - y_hat)).squeeze()/(len(y))

    def predict_(self, x):
        """_summary_

        Args:
            x (numpy.ndarray): a vector of dimension m * 1
        """
        if not isinstance(x, np.ndarray):
            return None
        if x.size == 0 or self.thetas.size == 0:
            return None
        return np.dot(np.insert(x, 0, np.array([1]), axis=1), self.thetas)

    def loss_elem_(self, y, y_hat):
        """_summary_

        Args:
            y (numpy.ndarray): a vector of dimension m * 1
            y_hat (numpy.ndarray): a vector of dimension m * 1
        """
        return np.square(y_hat - y)

    def loss_(self, y, y_hat):
        """_summary_

        Args:
            y (numpy.ndarray): a vector of dimension m * 1
            y_hat (numpy.ndarray): a vector of dimension m * 1
        """
        if not isinstance(y, np.ndarray) and not isinstance(y_hat, np.ndarray):
            return None
        if y.shape != y_hat.shape:
            return None
        loss = self.loss_elem_(y, y_hat)
        return np.sum(loss) / (2 * len(loss))
