"""
Write a class that contains all methods necessary to perform linear regression.
"""

import numpy as np

class MyLinearRegression():
    """
    Description:
    My personnal linear regression class to fit like a boss.
    """

    def __init__(self, thetas, alpha=0.001, max_iter=1000):
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
        if x.shape != y.shape or len(self.thetas) != 2:
            return None
        if x.size == 0 or y.size == 0 or self.thetas.size == 0:
            return None
        i = 0
        while i < self.max_iter:
            x_hat = np.insert(x, 0, np.array([1]), axis=1)
            j = (1/(len(y))) * x_hat.transpose() @ (x_hat @ self.thetas - y)
            self.thetas = self.thetas - self.alpha * j
            i += 1
        return self.thetas

    def predict_(self, x):
        """_summary_

        Args:
            x (numpy.ndarray): a vector of dimension m * 1
        """
        if not isinstance(x, np.ndarray) or not isinstance(self.thetas, np.ndarray):
            return None
        if x.size == 0 or self.thetas.size == 0:
            return None
        new_x = np.insert(x, 0, np.array([1]), axis=1)
        return new_x @ self.thetas

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
