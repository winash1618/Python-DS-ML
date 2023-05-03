"""
Introduction to Numpy library.
"""

import random
import numpy as np

class NumPyCreator(object):
    """
    Create a numpy array from different type of object.
    """
    def from_list(self, lst) -> any:
        """
        takes a list or nested lists and returns its corresponding
        Numpy array.
        """
        try:
            return np.array(lst, dtype=object)
        except ValueError:
            return None

    def from_tuple(self, tpl) -> any:
        """
        takes a tuple or nested tuples and returns its corresponding Numpy array.
        """
        return np.asarray(tpl)

    def from_iterable(self, itr) -> any:
        """
        takes an iterable and returns an array which contain all its elements.
        """
        return np.array(itr)

    def from_shape(self, shape, value=0):
        """
        returns an array filled with the same value.
        The first argument is a tuple which specifies the shape of the array, and the second
        argument specifies the value of the elements. This value must be 0 by default.
        """
        return np.full(shape, value, dtype=np.int32)

    def random(self, shape) -> any:
        """
        returns an array filled with random values. It takes as an
        argument a tuple which specifies the shape of the array.
        """
        return np.full(shape, random.randint)

    def identity(self, n) -> any:
        """
        returns an array representing the identity matrix of size n.
        """
        return np.identity(n, dtype=np.float32)
