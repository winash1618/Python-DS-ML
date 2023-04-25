"""
The goal of this exercise is to implement a context manager as a class. Thus you are
strongly encouraged to do some research about context manager.
- Resources: https://book.pythontips.com/en/latest/context_managers.html
"""

import csv

class CsvReader():
    """
    Implement a CsvReader class that opens, reads, and parses a CSV file. This class is
    then a context manager as class. In order to create it, your class requires a few built-in
    methods:
    	• __init__,
    	• __enter__,
    	• __exit__.
    It is mandatory to close the file once the process has completed. You are expected to
    handle properly badly formatted CSV file (i.e. handle the exception):
    • mistmatch between number of fields and number of records,
    • records with different length.
    """
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.csvfile = open(filename, "r", encoding="utf-8")
        self.csv_reader = csv.reader(self.csvfile, delimiter=sep)
        row = []
        data = []
        length = None
        if header:
            self.header = next(self.csv_reader)
        else:
            self.header = []
            row = next(self.csv_reader)
            data.append(row)
            length = len(row)
        self.data = []
        if skip_top:
            next(self.csv_reader)
        try:
            while True:
                row = next(self.csv_reader)
                if header and len(row) != len(self.header):
                    raise ValueError("wrong number of fields")
                if not header:
                    if len(row) != length:
                        raise ValueError("Wrong number of fields")
                data.append(row)
        except StopIteration:
            pass
        except ValueError as err:
            print(err)
            exit(1)
        self.data = data
        if skip_bottom:
            self.data = self.data[:-1]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print (exc_type, exc_val, exc_tb)
        self.csvfile.close()
        return True

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        return self.data

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        return self.header
