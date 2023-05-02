"""
SpatioTemporalData
"""


class SpatioTemporalData(object):
    """
    Write a class called SpatioTemporalData that takes a dataset (pandas.DataFrame)
    as argument in its constructor and implements the following methods:
    • when(location): takes a location as an argument and returns a list containing the
    years where games were held in the given location,
    • where(date): takes a date as an argument and returns the location where the
    Olympics took place in the given year.
    Args:
        object (Object): It is a class with special with that have all the special methods
        which can be inherited. 
    """

    def __init__(self, data):
        """class initializer

        Args:
            df (pandas.DatasFrame): dataset
        """
        self.data = data

    def when(self, location):
        """
        when(location): takes a location as an argument and returns a list containing the
        years where games were held in the given location,

        Args:
            location (string): game location
        """
        new_data = self.data[self.data['City'] == location].drop_duplicates(subset=[
                                                                            'City'])
        return new_data['Year'].tolist()

    def where(self, date):
        """takes a date as an argument and returns the location where the
        Olympics took place in the given year.

        Args:
            date (string): date
        """
        new_data = self.data[self.data['Year'] == date].drop_duplicates(subset=[
                                                                        'Year'])
        return new_data['City'].tolist()
