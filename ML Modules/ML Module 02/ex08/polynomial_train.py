"""
polynomial train
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from polynomial_model import add_polynomial_features
from multivariate_linear_model import MyLinearRegression as MyLR
data = pd.read_csv("are_blue_pills_magics.csv")
x = np.array(data[['Micrograms']])
y = np.array(data[['Score']])
i = 1
plt.scatter(x, y)
mse = []
thetas = [
            np.array([[-20],[ 160]]).reshape(-1,1),
            np.array([[-20],[ 160],[ -80]]).reshape(-1,1),
            np.array([[-20],[ 160],[ -80],[ 10]]).reshape(-1,1),
            np.array([[-20],[ 160],[ -80],[ 10],[ -1]]).reshape(-1,1),
            np.array([[1140],[ -1850],[ 1110],[ -305],[ 40],[ -2]]).reshape(-1,1),
            np.array([[9110],[ -18015],[ 13400],[ -4935],[ 966],[ -96.4],[ 3.86]]).reshape(-1,1)
        ]
while i < 6:
    x_ = add_polynomial_features(x, i)
    my_lr = MyLR(thetas[i - 1])
    my_lr.fit_(x_, y)
    y_pred = my_lr.predict_(x_)
    continuous_x = np.arange(np.min(x), np.max(x), 0.01).reshape(-1, 1)
    x_ = add_polynomial_features(continuous_x, i)
    y_ = my_lr.predict_(x_)
    mse.append(my_lr.mse_(y_pred, y))
    plt.plot(continuous_x, y_, color='orange')
    plt.show()
    plt.savefig('image')
    i += 1
plt.clf()
x = [i for i in range(1, 6)]
plt.bar(x, mse)
plt.savefig('bar')
