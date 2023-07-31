class calculator:
    """
    A simple calculator class with basic arithmetic operations.

    Attributes:
        v (list): A list of numeric values.

    Methods:
        __init__(v=[]):
            Initializes a new calculator instance with an optional list
            of values.

        __add__(obj):
            Performs element-wise addition of the calculator object with
            another object.

        __mul__(obj):
            Performs element-wise multiplication of the calculator object
            with another object.

        __sub__(obj):
            Performs element-wise subtraction of the calculator object
            by another object.

        __truediv__(obj):
            Performs element-wise division of the calculator object by
            another object.

        __repr__():
            Returns a string representation of the calculator object's
            list of values.
    """

    def __init__(self, v=[]):
        """
        Initializes a new calculator instance.

        Args:
            v (list, optional): A list of numeric values.
            Defaults to an empty list.
        """
        self.v = v

    def __add__(self, obj):
        """
        Performs element-wise addition of the calculator
        object with another object.

        Args:
            obj: The object to add to each element of
            the calculator object's list.

        Returns:
            calculator: A new calculator object with
            the result of element-wise addition.
        """
        return calculator([x + obj for x in self.v])

    def __mul__(self, obj):
        """
        Performs element-wise multiplication of the
        calculator object with another object.

        Args:
            obj: The object to multiply with each element
            of the calculator object's list.

        Returns:
            calculator: A new calculator object with the
            result of element-wise multiplication.
        """
        return calculator([x * obj for x in self.v])

    def __sub__(self, obj):
        """
        Performs element-wise subtraction of the calculator
        object by another object.

        Args:
            obj: The object to subtract from each element of
            the calculator object's list.

        Returns:
            calculator: A new calculator object with the
            result of element-wise subtraction.
        """
        return calculator([x - obj for x in self.v])

    def __truediv__(self, obj):
        """
        Performs element-wise division of the calculator
        object by another object.

        Args:
            obj: The object to divide each element of the
            calculator object's list by.

        Returns:
            calculator: A new calculator object with the
            result of element-wise division.
        """
        return calculator([x / obj for x in self.v])

    def __repr__(self):
        """
        Returns a string representation of the calculator
        object's list of values.

        Returns:
            str: A string representation of the list of values.
        """
        return str(self.v)
