"""
test
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from univariate_linear_model import MyLinearRegression as MyLR
data = pd.read_csv("spacecraft_data.csv")
X = np.array(data[['Age']])
Y = np.array(data[['Sell_price']])
myLR_age = MyLR(thetas = np.array([[1000.0], [-1.0]]), alpha = 2.5e-5, max_iter = 100000)
myLR_age.fit_(X[:,0].reshape(-1,1), Y)
y_pred = myLR_age.predict_(X[:,0].reshape(-1,1))
print(myLR_age.mse_(y_pred,Y))
plt.scatter(X, Y)
plt.scatter(X, y_pred)
plt.savefig('age')
plt.clf()
#Output
# 55736.86719...
X = np.array(data[['Thrust_power']])
myLR_Thrust = MyLR(thetas = np.array([[1.0], [1.1]]), alpha = 2.5e-5, max_iter = 100000)
myLR_Thrust.fit_(X[:,0].reshape(-1,1), Y)
y_pred = myLR_Thrust.predict_(X[:,0].reshape(-1,1))
print(myLR_Thrust.mse_(y_pred,Y))
plt.scatter(X, Y)
plt.scatter(X, y_pred)
plt.savefig('Thrust')
plt.clf()
#Output
# 25511.61674...
X = np.array(data[['Terameters']])
myLR_Terameters = MyLR(thetas = np.array([[901.0], [-1]]), alpha = 2.5e-5, max_iter = 100000)
myLR_Terameters.fit_(X[:,0].reshape(-1,1), Y)
y_pred = myLR_Terameters.predict_(X[:,0].reshape(-1,1))
print(myLR_Terameters.mse_(y_pred,Y))
plt.scatter(X, Y)
plt.scatter(X, y_pred)
plt.savefig('Terameters')
plt.clf()
#Output
# 38201.67316...