import numpy as np
from my_logistic_regression import MyLogisticRegression as mylogr
theta = np.array([[-2.4], [-1.5], [0.3], [-1.4], [0.7]])
# Example 1:
model1 = mylogr(theta, lambda_=5.0)
# model1.penalty
# Output
# 'l2'
# model1.lambda_
# Output
# 5.0
# Example 2:
model2 = mylogr(theta, penalty=None)
print(model2.theta)
# model2.penalty
# Output
# None
# model2.lambda_
# Output
# 0.0
# Example 3:
model3 = mylogr(theta, penalty=None, lambda_=2.0)
print(model3.theta)
# model3.penalty
# Output
# None
# model3.lambda_
# Output
# 0.0
