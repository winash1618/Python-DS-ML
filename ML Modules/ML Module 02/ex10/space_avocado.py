"""
space avocado best model
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def polynomial_features(x, degree):
    X_poly = np.zeros((len(x), degree+1))
    for i in range(degree+1):
        X_poly[:,i] = x.squeeze()**i
    return X_poly

def ridge_regression(X, y, alpha):
    I = np.eye(X.shape[1])
    I[0,0] = 0
    return np.linalg.inv(X.T @ X + alpha*I) @ X.T @ y

data = pd.read_csv('space_avocado.csv')

train_data = data[:round(len(data)*0.6)]
test_data = data[round(len(data)*0.8):]

# Load the models from the file
models_df = pd.read_csv('models.csv')
models = models_df.to_dict(orient='records')

# Find the best model
best_model = min(models, key=lambda x: x['error'])

# Train the best model
degree = best_model['degree']
alpha = best_model['alpha']
X_train_poly = polynomial_features(train_data['prod_distance'].values.reshape(-1, 1), degree)
y_train = train_data['target'].values.reshape(-1, 1)
theta = ridge_regression(X_train_poly, y_train, alpha)

# Evaluate the best model on the test set
X_test_poly = polynomial_features(test_data['prod_distance'].values.reshape(-1, 1), degree)
y_test = test_data['target'].values.reshape(-1, 1)
y_test_pred = X_test_poly @ theta
test_error = np.mean((y_test_pred - y_test)**2)

# Plot the true price and predicted price for different regularization factors
alphas = models_df['alpha'].unique()
plt.figure(figsize=(12, 8))
plt.scatter(test_data['prod_distance'], y_test, color='blue', label='True Price')
for alpha in alphas:
    theta_alpha = models_df.loc[models_df['alpha'] == alpha, 'theta'].values[0]
    y_pred = polynomial_features(test_data['prod_distance'].values.reshape(-1, 1), degree) @ theta_alpha
    plt.plot(test_data['prod_distance'], y_pred, label=f'Alpha={alpha:.1f}')
plt.xlabel('Distance')
plt.ylabel('Price')
plt.title('True Price vs Predicted Price')
plt.legend()
plt.show()

# Print the test error
print(f'Test Error: {test_error}')
