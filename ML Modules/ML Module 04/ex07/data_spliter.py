"""
data splitter
"""

import numpy as np

def data_spliter(x, y, proportion):
    """Shuffles and splits the dataset (given by x and y) into a training and a test set,
    while respecting the given proportion of examples to be kept in the training set.
    Args:
    x: has to be an numpy.array, a matrix of dimension m * n.
    y: has to be an numpy.array, a vector of dimension m * 1.
    proportion: has to be a float, the proportion of the dataset that will be assigned to the
    training set.
    Return:
    (x_train, x_test, y_train, y_test) as a tuple of numpy.array
    None if x or y is an empty numpy.array.
    None if x and y do not share compatible dimensions.
    None if x, y or proportion is not of expected type.
    Raises:
    This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray)\
        or not isinstance(proportion, float):
        return None
    if x.size == 0 or y.size == 0:
        return None
    m, n = x.shape
    k, l = y.shape
    if m != k or l != 1:
        return None
    arr = np.hstack(( y.reshape(-1, 1), x))
    np.random.shuffle(arr)
    split_len = int(proportion * len(y))
    train_set = arr[:split_len, :]
    test_set = arr[split_len:, :]
    return (train_set[:, 1:], test_set[:, 1:], train_set[:, 0].reshape(-1,1), test_set[:, 0].reshape(-1,1))
