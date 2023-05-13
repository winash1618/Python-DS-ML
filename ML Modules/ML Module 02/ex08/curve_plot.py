"""
test
"""
import numpy as np
import matplotlib.pyplot as plt
from polynomial_model import add_polynomial_features
from multivariate_linear_model import MyLinearRegression as MyLR
x = np.arange(1,11).reshape(-1,1)
y = np.array([[ 1.39270298],
[ 3.88237651],
[ 4.37726357],
[ 4.63389049],
[ 7.79814439],
[ 6.41717461],
[ 8.63429886],
[ 8.19939795],
[10.37567392],
[10.68238222]])
plt.scatter(x, y)
plt.show()
## To get a smooth curve, we need a lot of data points
x_ = add_polynomial_features(x, 3)
my_lr = MyLR(np.ones(4).reshape(-1, 1))
my_lr.fit_(x_, y)
continuous_x = np.arange(1, 10.01, 0.01).reshape(-1, 1)
x_ = add_polynomial_features(continuous_x, 3)
y_ = my_lr.predict_(x_)
# Plot:
plt.plot(continuous_x, y_, color='orange')
plt.scatter(continuous_x, y_)
plt.show()
plt.savefig('image')
