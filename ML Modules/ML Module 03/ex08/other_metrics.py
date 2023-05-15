
import numpy as np

def accuracy_score_(y, y_hat):
    """
    Compute the accuracy score.
    Args:
    y:a numpy.ndarray for the correct labels
    y_hat:a numpy.ndarray for the predicted labels
    Returns:
    The accuracy score as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    compare_arr = (y == y_hat)
    return(np.sum(compare_arr) / len(y))

def precision_score_(y, y_hat, pos_label=1):
    """
    Compute the precision score.
    Args:
    y:a numpy.ndarray for the correct labels
    y_hat:a numpy.ndarray for the predicted labels
    pos_label: str or int, the class on which to report the precision_score (default=1)
    Return:
    The precision score as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    tp = np.sum((y == y_hat) & (y == pos_label))
    fp = np.sum((y != y_hat) & (y != pos_label))
    return (tp / (tp + fp))

def recall_score_(y, y_hat, pos_label=1):
    """
    Compute the recall score.
    Args:
    y:a numpy.ndarray for the correct labels
    y_hat:a numpy.ndarray for the predicted labels
    pos_label: str or int, the class on which to report the precision_score (default=1)
    Return:
    The recall score as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    tp = np.sum((y == y_hat) & (y == pos_label))
    fn = np.sum((y != y_hat) & (y == pos_label))
    return (tp / (tp + fn))

def f1_score_(y, y_hat, pos_label=1):
    """
    Compute the f1 score.
    Args:
    y:a numpy.ndarray for the correct labels
    y_hat:a numpy.ndarray for the predicted labels
    pos_label: str or int, the class on which to report the precision_score (default=1)
    Returns:
    The f1 score as a float.
    None on any error.
    Raises:
    This function should not raise any Exception.
    """
    return (2 * precision_score_(y, y_hat, pos_label) * recall_score_(y, y_hat, pos_label)) / (precision_score_(y, y_hat, pos_label) + recall_score_(y, y_hat, pos_label))