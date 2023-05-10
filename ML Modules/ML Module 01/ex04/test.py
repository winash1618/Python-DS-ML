"""
Evaluate a linear regression model on a very small dataset, with a given hypothesis
function h. Manipulate the loss function J, plot it, and briefly analyze the plot.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from linear_model import MyLinearRegression as MyLR
data = pd.read_csv("./are_blue_pills_magic.csv")
Xpill = np.array(data['Micrograms']).reshape(-1,1)
Yscore = np.array(data['Score']).reshape(-1,1)
linear_model1 = MyLR(np.array([[89.0], [-8]]))
linear_model2 = MyLR(np.array([[89.0], [-6]]))
Y_model1 = linear_model1.predict_(Xpill)
Y_model2 = linear_model2.predict_(Xpill)
plt.scatter(Xpill, Yscore)
plt.plot(Xpill, Y_model1)
plt.scatter(Xpill, Y_model1)
plt.savefig('image.png')

print(linear_model1.mse_(Yscore, Y_model1))
# 57.60304285714282
print(mean_squared_error(Yscore, Y_model1))
# 57.603042857142825
print(linear_model2.mse_(Yscore, Y_model2))
# 232.16344285714285
print(mean_squared_error(Yscore, Y_model2))
# 232.16344285714285

def mse_(self, y, y_hat):
    """_summary_

    Args:
        y (numpy.ndarray): a vector of dimension m * 1
        y_hat (numpy.ndarray): a vector of dimension m * 1
    """
    if not isinstance(y, np.ndarray) and not isinstance(y_hat, np.ndarray):
        return None
    if y.shape != y_hat.shape:
        return None
    if y.size == 0 or y_hat.size == 0:
        return None
    return np.squeeze((1 / len(y)) * ((y_hat - y).transpose() @ (y_hat - y)))

thetas = np.linspace(-30, 11, 100)
C = np.linspace(0.2, .9, 5)
for c in C:
    J_vals = []
    for theta in thetas:
        J_vals.append(np.mean((Yscore - c * theta + theta * Xpill) ** 2))
    J_array = np.array(J_vals)
    plt.plot(thetas, J_array)
plt.savefig('image2.png')