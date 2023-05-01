"""The goal of this exercise is to create a Fileloader class containing a load and a display
method.
"""

import pandas as pd


class FileLoader(object):
    """Load and display a file

    Args:
        object (Object): Allow us to acces built in special method associate with object.
    """

    def load(self, path):
        """Load dataset from a file into pandas.DataFrame
        takes as an argument the file path of the dataset to load,
        displays a message specifying the dimensions of the dataset (e.g. 340 x 500) and
        returns the dataset loaded as a pandas.DataFrame.
        Args:
            path (string): file path of the dataset to load
        """
        df = pd.read_csv(path)
        print(df.shape)
        return df

    def display(self, df, n):
        """takes a pandas.DataFrame and an integer as arguments,
        displays the first n rows of the dataset if n is positive, or the last n rows if n is
        negative.

        Args:
            df (pandas.DataFrame): DataFrame object
            n (int): rows
        """
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(abs(n)))
