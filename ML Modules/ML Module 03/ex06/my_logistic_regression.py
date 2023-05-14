"""
Logistic regression class
"""

import numpy as np

class MyLogisticRegression():
    """
    Description:
    My personnal logistic regression to classify things.
    """
    def __init__(self, theta, alpha=0.001, max_iter=1000):
        """_summary_

        Args:
            theta (_type_): _description_
            alpha (float, optional): _description_. Defaults to 0.001.
            max_iter (int, optional): _description_. Defaults to 1000.
        """
        self.alpha = alpha
        self.max_iter = max_iter
        self.theta = theta
    def predict_(self, x):
        """_summary_

        Args:
            x (_type_): _description_

        Returns:
            _type_: _description_
        """
        X = np.insert(x, 0, np.array([1]), axis=1)
        return (1 / (1 + np.exp(np.dot(-X, self.theta))))
    def loss_(self, x, y):
        """loss

        Args:
            y (_type_): _description_
            y_hat (_type_): _description_

        Returns:
            _type_: _description_
        """
        y_hat = self.predict_(x)
        eps = 1e-15
        epsm = np.full(y.shape, eps)
        ones = np.ones(y.shape)
        y_safe = y + epsm
        y_hatsafe = y_hat + epsm
        print(y_safe, y_hatsafe)
        print( ones - y_hatsafe)
        # return (-1/y.shape[0]) * (np.dot(y.transpose(), np.log(y_hatsafe)) \
        #     + np.dot((ones - y_safe).transpose(), np.log(ones - y_hatsafe))).squeeze()
    def fit_(self, x, y):
        """fit

        Args:
            x (_type_): _description_
            y (_type_): _description_
        """
        i = 0
        while i < self.max_iter:
            X = np.insert(x, 0, np.array([1]), axis=1)
            y_hat = 1 / (1 + np.exp(-np.ones(y.shape) * np.dot(X, self.theta)))
            grad = (1 / x.shape[0]) * np.dot(X.transpose(), y_hat - y).squeeze()
            self.theta = self.theta - self.alpha * grad
            i += 1
