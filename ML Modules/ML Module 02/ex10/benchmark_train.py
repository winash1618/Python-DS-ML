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
my_lr = MyLR(np.array([[24], [1], [1444], [2]]))
print(my_lr.fit_(train_set_x, train_set_y))
