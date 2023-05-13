import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from multivariate_linear_model import MyLinearRegression as MyLR
data = pd.read_csv("spacecraft_data.csv")
X = np.array(data[['Age','Thrust_power','Terameters']])
Y = np.array(data[['Sell_price']])
my_lreg = MyLR(thetas = np.array([[1.0], [1.0], [1.0], [1.0]]) , alpha = 0.0000732, max_iter = 600000)
# Example 0:
print(my_lreg.mse_(X,Y))
# Output:
# 144044.877...
# Example 1:
my_lreg.fit_(X,Y)
print(my_lreg.thetas)
# Output:
# array([[334.994...],[-22.535...],[5.857...],[-2.586...]])
# Example 2:
print(my_lreg.mse_(X,Y))
# Output:
# 586.896999...

Age = np.array(data[['Age']])
Thrust_power = np.array(data[['Thrust_power']])
Terameters = np.array(data[['Terameters']])
y_pred = my_lreg.predict_(X)

plt.scatter(Age, Y)
plt.scatter(Age, y_pred)
plt.savefig('AgeM')
plt.clf()
plt.scatter(Thrust_power, Y)
plt.scatter(Thrust_power, y_pred)
plt.savefig('ThrustM')
plt.clf()
plt.scatter(Terameters, Y)
plt.scatter(Terameters, y_pred)
plt.savefig('TerametersM')
