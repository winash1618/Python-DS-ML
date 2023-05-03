"""
The goal of the exercise is to get you used with built-in methods, more particularly with
those allowing to perform operations. Student is expected to code built-in methods for
vector-vector and vector-scalar operations as rigorously as possible.
"""


class Vector:
    """
    create a Vector class. The goal is to create vectors and be
    able to perform mathematical operations with them.
        • Column vectors are represented as list of lists of single float ([[1.], [2.], [3.]]),
        • Row vectors are represented as a list of a list of several floats ([[1., 2., 3.]]).
    The class should also has 2 attributes:
        • values: list of list of floats (for row vector) or list of lists of single float (for column
        vector),
        • shape: tuple of 2 integers: (1,n) for a row vector of dimension n or (n,1) for a
        column vector of dimension n.
    Finally you have to implement 2 methods:
        • .dot() produce a dot product between two vectors of same shape,
        • .T() returns the transpose vector (i.e. a column vector into a row vector, or a row
        vector into a column vector).
    """

    def __init__(self, value1=None, value2=None):
        """
        To be called automatically when Vector class is 
        instantiated with row vector or colomn vector.
        """
        if value1 is not None and value2 is not None:
            if value1 > value2:
                print("Invalid arguments: start should be less than end")
                self.values = []
                self.shape = (0, 0)
            else:
                self.values = [[float(value)]
                               for value in range(value1, value2)]
                self.shape = (value2 - value1, 1)
        elif value1 is not None:
            if isinstance(value1, (int)):
                self.values = [[float(i)] for i in range(value1)]
                self.shape = (value1, 1)
            else:
                self.values = value1
                if len(value1) == 1:
                    self.shape = (1, len(value1[0]))
                else:
                    self.shape = (len(value1), 1)
        else:
            print("Invalid arguments: provide values, size, or start and end")
            self.values = []
            self.shape = (0, 0)

    def __add__(self, other) -> 'Vector':
        if isinstance(other, Vector):
            if self.shape[0] == other.shape[0] and self.shape[1] == other.shape[1]:
                if self.shape[0] == 1:
                    new_vector = []
                    for value1, value2 in zip(self.values[0], other.values[0]):
                        new_vector.append([value1 + value2])
                    return new_vector
                else:
                    new_vector = []
                    for value1, value2 in zip(self.values. other.values):
                        new_vector.append([value1[0] + value2[0]])
                    return new_vector
        raise NotImplementedError("Type unknown")

    def __radd__(self, other) -> 'Vector':
        if isinstance(other, (int, float)):
            if self.shape[0] == 1:
                new_vector = []
                for value in self.values[0]:
                    new_vector.append([value + other])
                return new_vector
            else:
                new_vector = []
                for value in self.values:
                    new_vector.append([value[0] + other])
                return new_vector
        raise NotImplementedError("Type unknown")

    def __sub__(self, other) -> 'Vector':
        if isinstance(other, Vector):
            if self.shape[0] == other.shape[0] and self.shape[1] == other.shape[1]:
                if self.shape[0] == 1:
                    new_vector = []
                    for value1, value2 in zip(self.values[0], other.values[0]):
                        new_vector.append([value1 - value2])
                    return new_vector
                else:
                    new_vector = []
                    for value1, value2 in zip(self.values. other.values):
                        new_vector.append([value1[0] - value2[0]])
                    return new_vector
        raise NotImplementedError("Type unknown")

    def __rsub__(self, other) -> 'Vector':
        if isinstance(other, (int, float)):
            if self.shape[0] == 1:
                new_vector = []
                for value in self.values[0]:
                    new_vector.append([other - value])
                return new_vector
            else:
                new_vector = []
                for value in self.values:
                    new_vector.append([other - value[0]])
                return new_vector
        raise NotImplementedError("Type unknown")

    def __truediv__(self, other) -> 'Vector':
        try:
            if isinstance(other, (int, float)):
                if self.shape[0] == 1:
                    print(self.shape)
                    new_vector = []
                    for value in self.values[0]:
                        new_vector.append(value / other)
                    return [new_vector]
                else:
                    new_vector = []
                    for value in self.values:
                        new_vector.append([value[0] / other])
                    return new_vector
        except NotImplementedError as err:
            print("NotImplementedError", err)
        except ZeroDivisionError as err:
            print("ZeroDivisionError:", err)

    def __rtruediv__(self, other) -> 'Vector':
        print("NotImplementedError: Division of a scalar by a Vector is not defined here.")

    def __mul__(self, other) -> 'Vector':
        if isinstance(other, (int, float)):
            if self.shape[0] == 1:
                new_vector = []
                for value in self.values[0]:
                    new_vector.append(value * other)
                return [new_vector]
            else:
                new_vector = []
                for value in self.values:
                    new_vector.append([value[0] * other])
                return new_vector
        raise NotImplementedError("Type unknown")

    def __rmul__(self, other) -> 'Vector':
        if isinstance(other, (int, float)):
            if self.shape[0] == 1:
                new_vector = []
                for value in self.values[0]:
                    new_vector.append([value * other])
                return new_vector
            else:
                new_vector = []
                for value in self.values:
                    new_vector.append([value[0] * other])
                return new_vector
        raise NotImplementedError("Type unknown")

    def __str__(self) -> str:
        """
        Return the string to vector info
        """
        return f"{self.values}"

    def __repr__(self) -> str:
        """
        It return the vector representation in string form
        """
        if self.shape[0] == 1:
            rep = "["
            count = 0
            for value in self.values[0]:
                count += 1
                if len(self.values[0]) == count:
                    rep += f"[{value}]"
                else:
                    rep += f"[{value}], "
            rep += "]"
        else:
            rep = "["
            count = 0
            for value in self.values:
                count += 1
                if len(self.values) == count:
                    rep += f"[{value[0]}]"
                else:
                    rep += f"[{value}], "
            rep += "]"
        return rep

    def T(self) -> any:
        """
        returns the transpose vector (i.e. a column vector into a row vector, or a row
        vector into a column vector).
        """
        new_values = []
        if self.shape[0] == 1:
            for value in self.values[0]:
                new_values.append([float(value)])
            return Vector(new_values)
        else:
            for value in self.values:
                new_values.append(float(value[0]))
            return Vector([new_values])

    def dot(self, other: any) -> any:
        """
        produce a dot product between two vectors of same shape,
        """
        if sum(self.shape) == sum(other.shape):
            total = 0
            if self.shape[0] == 1:
                if other.shape[0] == 1:
                    for value1, value2 in zip(self.values[0], other.values[0]):
                        total += float(value1 * value2)
                    return total
                else:

                    for value1, value2 in zip(self.values[0], other.values):
                        total += float(value1 * value2[0])
                    return total
            else:
                if other.shape[0] == 1:
                    for value1, value2 in zip(self.values, other.values[0]):
                        total += float(value1[0] * value2)
                    return total
                else:
                    for value1, value2 in zip(self.values, other.values):
                        total += float(value1[0] * value2[0])
                    return total
        else:
            raise NotImplementedError(
                "dot product not implemented for this check your input")
