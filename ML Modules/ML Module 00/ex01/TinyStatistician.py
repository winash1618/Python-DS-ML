"""
Initiation to very basic statistic notions.
"""

import math


class TinyStatistician(object):
    """
    A class to do some statistic operations.
    """

    def mean(self, x) -> any:
        """
        computes the mean of a given non-empty list or array x, using a for-loop.
        The method returns the mean as a float, otherwise None if x is an empty list or
        array.
        """
        if len(x):
            return sum(x) / len(x)
        else:
            return None

    def median(self, x) -> any:
        """
        computes the median of a given non-empty list or array x. The method
        returns the median as a float, otherwise None if x is an empty list or array.
        """
        if len(x):
            x.sort()
            if len(x) % 2 == 0:
                return (x[int(len(x) / 2)] + x[int((len(x) / 2) + 1)]) / 2
            else:
                return x[int(len(x) / 2)]
        else:
            return None

    def quartile(self, x) -> any:
        """
        computes the 1st and 3rd quartiles of a given non-empty array x. The
        method returns the quartile as a float, otherwise None if x is an empty list or
        array.
        """
        q1 = 0
        q3 = 0
        if len(x):
            if (len(x) * (1 / 4) % 2) == 0:
                q1 = (x[int(len(x) * (1 / 4))] +
                      x[int(len(x) * (1 / 4) + 1)]) / 2
            else:
                q1 = x[int(len(x) * (1 / 4))]
            if (len(x) * (3 / 4) % 2) == 0:
                q3 = (x[int(len(x) * (3 / 4))] +
                      x[int(len(x) * (3 / 4) + 1)]) / 2
            else:
                q3 = x[int(len(x) * (3 / 4))]
        else:
            return None
        return [q1, q3]

    def percentile(self, x, p):
        """computes the expected percentile of a given non-empty list or
        array x. The method returns the percentile as a float, otherwise None if x is an
        empty list or array or a non expected type object. The second parameter is the
        wished percentile. This method should not raise any Exception.

        Args:
            x (list): list of data
            p (float): wished percentile
        """
        if isinstance(x, (list, tuple)) and len(x) > 0 and isinstance(p, (float, int)) and 0 <= p <= 100:
            sorted_x = sorted(x)
            k = (len(x) - 1) * (float(p) / 100)
            f = int(k)
            c = f + 1
            if c >= len(x):
                return sorted_x[-1]
            else:
                return sorted_x[f] + (sorted_x[c] - sorted_x[f]) * (k - f)
        else:
            return None
    def var(self, x) -> any:
        """
        computes the variance of a given non-empty list or array x, using a forloop.
        The method returns the variance as a float, otherwise None if x is an empty list or array.
        """
        mean = self.mean(x)
        variance = 0
        if len(x):
            for element in x:
                variance += (element - mean)**2
            variance = variance / (len(x) - 1)
            return variance
        else:
            return None

    def std(self, x) -> any:
        """
        computes the standard deviation of a given non-empty list or array x,
        using a for-loop. The method returns the standard deviation as a float, otherwise
        None if x is an empty list or array. 
        """
        if len(x):
            return math.sqrt(self.var(x))
        else:
            return None
