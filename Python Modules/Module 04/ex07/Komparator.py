"""
The goal the exercise is to introduce plotting methods among the different libraries
Pandas, Matplotlib, Seaborn or Scipy.
"""


class Komparator(object):
    """
    Write a class called Komparator whose constructor takes as an argument a pandas.
    DataFrame which contains the dataset. The class must implement the following
    methods, which take as input two variable names:

    Args:
        object (Object): object (Object): It is a class with special with that have all the special methods
        which can be inherited. 
    """

    def __init__(self, data):
        self.data = data

    def compare_box_plots(self, categorical_var, numerical_var):
        """ displays a series of box plots to compare how the distribution of the numerical variable changes
        if we only consider the subpopulation which belongs to each category. There should
        be as many box plots as categories. For example, with Sex and Height, we would
        compare the height distributions of men vs. women with two box plots.

        Args:
            categorical_var (_type_): _description_
            numerical_var (_type_): _description_
        """

    def density(self, categorical_var, numerical_var):
        """displays the density of the numerical variable. 
        Each subpopulation should be represented by a separate curve
        on the graph.

        Args:
            categorical_var (_type_): _description_
            numerical_var (_type_): _description_
        """

    def compare_histograms(self, categorical_var, numerical_var):
        """
        plots the numerical variable in a separate histogram for each category. 
        As an extra, you can use overlapping histograms with a color code.

        Args:
            categorical_var (_type_): _description_
            numerical_var (_type_): _description_
        """
