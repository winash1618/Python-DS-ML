from sklearn.metrics import confusion_matrix
import numpy as np
from confusion_matrix import confusion_matrix_
y_hat = np.array([['norminet'], ['dog'], ['norminet'], ['norminet'], ['dog'], ['bird']])
y = np.array([['dog'], ['dog'], ['norminet'], ['norminet'], ['dog'], ['norminet']])
# Example 1:
## your implementation
print(confusion_matrix_(y, y_hat))
## Output:
# array([[0 0 0]
# [0 2 1]
# [1 0 2]])
## sklearn implementation
confusion_matrix(y, y_hat)
## Output:
# array([[0 0 0]
# [0 2 1]
# [1 0 2]])
# Example 2:
## your implementation
print(confusion_matrix_(y, y_hat, labels=['dog', 'norminet']))
## Output:
# array([[2 1]
# [0 2]])
## sklearn implementation
confusion_matrix(y, y_hat, labels=['dog', 'norminet'])
## Output:
# array([[2 1]
# [0 2]])