"""
Training Benchmark Models
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from polynomial_model import add_polynomial_features
from multivariate_linear_model import MyLinearRegression as MyLR
from data_spliter import data_spliter
data = pd.read_csv("space_avocado.csv")
x = np.array(data[['weight', 'prod_distance', 'time_delivery']])
y = np.array(data[['target']])
train_set_x, test_set_x, train_set_y, test_set_y = data_spliter(x, y, 0.8)
# print(train_set_x, test_set_x, train_set_y, test_set_y)
# my_lr = MyLR(np.array([[24], [1], [1444], [2]]))
thetas = np.array([[24], [1], [1444], [2], [432]])
# print(my_lr.fit_(train_set_x, train_set_y))
degrees = [1, 2, 3, 4]
alphas = np.arange(0, 1.2, 0.2)

models = []

i = 2
for degree in degrees:
    train_set_X = add_polynomial_features(train_set_x[:, 1].reshape(-1, 1), degree)
    train_set_Y = train_set_y.reshape(-1, 1)
    test_set_X = add_polynomial_features(test_set_x[:, 1].reshape(-1, 1), degree)
    test_set_Y = test_set_y.reshape(-1, 1)
    print(train_set_X)
    print(train_set_Y)
    print(test_set_X)
    print(test_set_Y)
    theta = thetas[:i]
    for alpha in alphas:
        mylr = MyLR(theta, alpha)
        theta = mylr.fit_(train_set_X, train_set_Y)
        y_hat = mylr.predict_(test_set_X)
        error = np.mean((y_hat - test_set_Y)**2)
        models.append({'degree': degree, 'alpha': alpha, 'theta': theta, 'error': error})
        print(models)
    i += 1

# Save the models to a file
models_df = pd.DataFrame(models)
models_df.to_csv('models.csv', index=False)