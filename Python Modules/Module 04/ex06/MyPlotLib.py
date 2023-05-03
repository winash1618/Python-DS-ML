"""
The goal the exercise is to introduce plotting methods among the different libraries Pandas, Matplotlib, Seaborn or Scipy.
"""

import matplotlib.pyplot as plt
import seaborn as sns


class MyPlotLib(object):
    """
    Write a class called MyPlotLib. This class implements different plotting methods,
    each of which take two arguments:
    • a pandas.DataFrame which contains the dataset,
    • a list of feature names.

    Args:
        object (Object): It is a class with special with that have all the special methods
        which can be inherited. 
    """

    def histogram(self, data, features):
        """plots one histogram for each numerical feature in
        the list,

        Args:
            data (data.DataFrame): dataset
            features (list): features
        """
        for feature in features:
            data[feature].hist()
            plt.savefig('histogram')
        plt.clf()

    def density(self, data, features):
        """plots the density curve of each numerical feature in
        the list,

        Args:
            data (data.DataFrame): dataset
            features (list): features
        """
        for feature in features:
            data[feature].plot.density()
            plt.savefig('density')
        plt.clf()

    def pair_plot(self, data, features):
        """plots a matrix of subplots (also called scatter plot
        matrix). On each subplot shows a scatter plot of one numerical variable against
        another one. The main diagonal of this matrix shows simple histograms.

        Args:
            data (data.DataFrame): dataset
            features (list): features
        """
        for feature in features:
            sns.pairplot(data[features], hue=feature)
            plt.savefig(feature)
        plt.clf()

    def box_plot(self, data, features):
        """ displays a box plot for each numerical variable in the
        dataset.

        Args:
            data (data.DataFrame): dataset
            features (list): features
        """
        data[features].boxplot()
        plt.savefig('box_plot')
        plt.clf()
