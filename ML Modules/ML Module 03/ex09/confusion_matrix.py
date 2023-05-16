
import numpy as np

def confusion_matrix_(y_true, y_hat, labels=None):
    """
    Compute confusion matrix to evaluate the accuracy of a classification.
    Args:
    y:a numpy.array for the correct labels
    y_hat:a numpy.array for the predicted labels
    labels: optional, a list of labels to index the matrix.
    This may be used to reorder or select a subset of labels. (default=None)
    df_option: optional, if set to True the function will return a pandas DataFrame
    instead of a numpy array. (default=False)
    Return:
    The confusion matrix as a numpy array or a pandas DataFrame according to df_option value.
    None if any error.
    Raises:
    This function should not raise any Exception.
    """
    if labels is None:
        labels=['bird', 'dog', 'norminet']
    arr = np.zeros((len(labels),len(labels)))
    print(arr)
    for (i, j), _ in np.ndenumerate(arr):
        pair = (labels[i], labels[j])
        count = sum([pair == elem for elem in zip(y_true.flat, y_hat.flat)])
        arr[i,j] = count
    return arr
