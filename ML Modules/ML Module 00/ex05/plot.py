"""
You must implement a function to plot the data and the prediction line (or regression
line). You will plot the data points (with their x and y values), and the prediction line
that represents your hypothesis (hθ).
"""

import matplotlib.pyplot as plt
from prediction import predict_

def plot(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.array.
    Args:
    x: has to be an numpy.array, a vector of dimension m * 1.
    y: has to be an numpy.array, a vector of dimension m * 1.
    theta: has to be an numpy.array, a vector of dimension 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exceptions.
    """
    
    plt.scatter(x, y)
    plt.plot(x, predict_(x, theta))
    plt.savefig('image.png')
