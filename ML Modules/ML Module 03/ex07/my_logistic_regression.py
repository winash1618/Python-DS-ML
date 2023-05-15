"""
Logistic regression class
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
        """loas

        Args:
            x (_type_): _description_
            y (_type_): _description_

        Returns:
            _type_: _description_
        """
        if not isinstance(x, np.ndarray) or \
            not isinstance(y, np.ndarray):
            return None
        if y.size == 0 or x.size == 0:
            return None
        vec_func = np.vectorize(value_corrector)
        y_hatsafe = vec_func(self.predict_(x))
        loss = (-1/y.shape[0]) * (np.dot(y.transpose(), np.log(y_hatsafe)) \
                         + np.dot(1 - y.transpose(), np.log(1 - y_hatsafe)))
        return loss.item()

    def fit_(self, x, y):
        """fit

        Args:
            x (_type_): _description_
            y (_type_): _description_
        """
        i = 0
        while i < self.max_iter:
            y_hat = self.predict_(x)
            X = np.insert(x, 0, np.array([1]), axis=1)
            grad = (1 / x.shape[0]) * np.dot(X.transpose(), y_hat - y)
            self.theta = self.theta - self.alpha * grad
            i += 1
