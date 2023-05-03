# Import the Matrix and Vector classes
from matrix import Matrix, Vector

# Create a matrix
m1 = Matrix([[1, 2], [3, 4]])

# Create another matrix
m2 = Matrix((2, 2))

# # Check the shape of the matrices
assert m1.shape == (2, 2)
assert m2.shape == (2, 2)

# Check the data of the matrices
assert m1.data == [[1, 2], [3, 4]]
assert m2.data == [[0, 0], [0, 0]]

# Test matrix addition
m3 = m1 + m2
assert m3.data == [[1, 2], [3, 4]]

# Test matrix subtraction
m4 = m1 - m2
assert m4.data == [[1, 2], [3, 4]]

m10 = 4 / m1
print(m10.data)

# Test matrix multiplication by scalar
m5 = m1 * 2
assert m5.data == [[2, 4], [6, 8]]
# print(m5.data)

m11 = m1 * m5
print(m11.data)

m122 = Matrix([[3, 34, 4, 45], [4, 2, 0, 53], [4, 2, 12, 3]])

m123 = m122.T()
print(m123.data)
# Create a vector
v1 = Vector([[1], [2], [3]])

# Create another vector
v2 = Vector([[1], [1], [1]])

v3 = Vector([[1, 3, 4]])


# Test vector dot product
assert v1.dot(v2) == 6

print(v1.dot(v2))
# Test matrix transpose
m6 = Matrix([[1, 2, 3], [4, 5, 6]])
m111 = Matrix([[1, 2, 3], [4, 5, 6], [1, 1, 1]])
assert m6.T().data == [[1, 4], [2, 5], [3, 6]]

# print((m111 * v1).data)
print((v3 * m111).data)


