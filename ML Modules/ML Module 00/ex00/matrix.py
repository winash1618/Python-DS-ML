"""
Manipulation and understanding of basic matrix operations.
In this exercise, you have to create a Matrix and a Vector class. The goal is to have matrices and be able to perform both matrix-matrix operation and matrix-vector operations
with them.
"""

class Matrix(object):
    """
    Your Matrix class must have the following 2 attributes:
    • data: list of lists
    • shape: the dimensions of the matrix as a tuple (rows, columns)
    You should be able to initialize the object with either:
    • the elements of the matrix as a list of lists: Matrix([[1.0, 2.0], [3.0, 4.0]])
    • a shape: Matrix((3, 3)) (the matrix will be filled with zeros by default)

    Args:
        object (Object): It is a builtin class, that can be inherited.
    """

    def __init__(self, data=None):
        if isinstance(data, list):
            row_len = len(data[0])
            for row in data:
                if not isinstance(row, list) or len(row) != row_len:
                    raise ValueError("Length of the list is not uniform")
                self.data = data
                self.shape = (len(data), len(data[0]))
        elif isinstance(data, tuple):
            self.data = [[0 for j in range(data[1])] for i in range(data[0])]
            self.shape = data
        else:
            raise NotImplementedError("Type unknown")

    def __add__(self, other):
        if isinstance(other, Matrix) and other.shape == self.shape:
            result = []
            for row1, row2 in zip(self.data, other.data):
                result_row = [x + y for x, y in zip(row1, row2)]
                result.append(result_row)
            return Matrix(result)
        else:
            raise NotImplementedError("Type unknown")

    def __radd__(self, other):
        if isinstance(other, Matrix) and other.shape == self.shape:
            result = []
            for row1, row2 in zip(other.data, self.data):
                result_row = [x + y for x, y in zip(row1, row2)]
                result.append(result_row)
            return Matrix(result)
        else:
            raise NotImplementedError("Type unknown")

    def __sub__(self, other):
        if isinstance(other, Matrix) and other.shape == self.shape:
            result = []
            for row1, row2 in zip(self.data, other.data):
                result_row = [x - y for x, y in zip(row1, row2)]
                result.append(result_row)
            return Matrix(result)
        else:
            raise NotImplementedError("Type unknown")

    def __rsub__(self, other):
        if isinstance(other, Matrix) and other.shape == self.shape:
            result = []
            for row1, row2 in zip(other.data, self.data):
                result_row = [x - y for x, y in zip(row1, row2)]
                result.append(result_row)
            return Matrix(result)
        else:
            raise NotImplementedError("Type unknown")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            result = []
            for row in self.data:
                result_row = [x / other for x in row]
                result.append(result_row)
            return Matrix(result)
        else:
            raise NotImplementedError("Type unknown")

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            result = []
            for row in self.data:
                result_row = [other / x for x in row]
                result.append(result_row)
            return Matrix(result)
        else:
            raise NotImplementedError("Type unknown")

    def __mul__(self, other):
        print(type(other))
        if isinstance(other, (int, float)):
            result = []
            for row in self.data:
                result_row = [x * other for x in row]
                result.append(result_row)
            return Matrix(result)
        elif isinstance(other, (Vector, Matrix)) and self.shape[1] == other.shape[0]:
            result = []
            for row1 in self.data:
                result_row = []
                for row2 in other.T().data:
                    value = 0
                    for x, y in zip(row1, row2):
                        value += x * y
                    result_row.append(value)
                result.append(result_row)
            if isinstance(other, Vector):
                return Vector(result)
            return Matrix(result)
        else:
            raise NotImplementedError("Type unknown")

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            result = []
            for row in self.data:
                result_row = [other * x for x in row]
                result.append(result_row)
            return Matrix(result)
        else:
            raise NotImplementedError("Type unknown")

    def T(self) -> any:
        """
        returns the transpose vector (i.e. a column vector into a row vector, or a row
        vector into a column vector).
        """
        result = []
        for i in range(len(self.data[0])):
            result_row = []
            for _, row in enumerate(self.data):
                result_row.append(row[i])
            result.append(result_row)
        return Matrix(result)

class Vector(Matrix):
    """Implements vector

    Args:
        Matrix (Matrix): matrix class
    """

    def __init__(self, data):
        if not isinstance(data, list):
            raise NotImplementedError("data is not a list")
        row_len = len(data[0])
        for row in data:
            if not isinstance(row, list) or len(row) != row_len:
                raise ValueError("Length of the list is not uniform")
        super().__init__(data)

    def dot(self, other):
        """DOT PRODUCT

        Args:
            other (Vector): Vector Object
        """
        if not isinstance(other, Vector):
            raise NotImplementedError("Only Vector Objects can be used")
        if sum(self.shape) == sum(other.shape):
            total = 0
            if self.shape[0] == 1:
                if other.shape[0] == 1:
                    for value1, value2 in zip(self.data[0], other.data[0]):
                        total += float(value1 * value2)
                    return total
                else:
                    for value1, value2 in zip(self.data[0], other.data):
                        total += float(value1 * value2[0])
                    return total
            else:
                if other.shape[0] == 1:
                    for value1, value2 in zip(self.data, other.data[0]):
                        total += float(value1[0] * value2)
                    return total
                else:
                    for value1, value2 in zip(self.data, other.data):
                        total += float(value1[0] * value2[0])
                    return total
        else:
            raise NotImplementedError(
                "dot product not implemented for this, check your input")
