"""
Ridge Regression
"""

import numpy as np
from MyLinearRegression import MyLinearRegression as MyLR

class MyRidge(MyLR):
    """
    Description:
    My personnal ridge regression class to fit like a boss.
    """
    def __init__(self, thetas, alpha=0.001, max_iter=1000, lambda_=0.5):
        super().__init__(thetas=thetas, alpha=alpha, max_iter=max_iter)
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas
        self.lambda_ = lambda_
    def get_params_(self):
        print("thetas = ", self.thetas)
        print("alpha = ", self.alpha)
        print("max_iter = ", self.max_iter)
        print("lambda = ", self.lambda_)
    def set_params_(self, thetas, alpha, max_iter, lambda_):
        self.alpha = alpha
        self.max_iter = max_iter
        self.thetas = thetas
        self.lambda_ = lambda_
    def loss_(self, y, y_hat):
        if not isinstance(y, np.ndarray) or not isinstance(y_hat, np.ndarray):
            return None
        if y.size == 0 or y_hat.size == 0:
            return None
        if y.shape != y_hat.shape:
            return None
        m, _ = y.shape
        thetas_ = np.array(self.thetas)
        thetas_[0] = 0
        return ((1 / (2 * m)) * (np.dot((y_hat - y).transpose(), y_hat - y) + self.lambda_ * thetas_.transpose() @ thetas_)).item()
    def gradient_(self, y, x):
        if not isinstance(y, np.ndarray) or not isinstance(x, np.ndarray):
            return None
        if y.size is 0 or x.size is 0:
            return None
        m, _ = x.shape
        X = np.insert(x, 0, np.array([1]), axis=1)
        theta_ = np.array(self.thetas)
        theta_[0] = 0
        return (1 / m) * (np.dot(X.transpose(), (self.predict_(x) - y)) + (self.lambda_ * theta_))
    def fit_(self, x, y):
        if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
            return None
        if x.size is 0 or y.size is 0:
            return None
        i = 0
        m, _ = y.shape
        thetas_ = np.array(self.thetas)
        while i < self.max_iter:
            X = np.insert(x, 0, np.array([1]), axis=1)
            j = (1 / m) * X.transpose @ (X @ thetas_ - y)
            thetas_ = thetas_ - self.alpha * j
            i += 1
        return thetas_
            
            
