# Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.
def determinant(matrix):
    temp = []
    if len(matrix) > 2:
        for i in range(len(matrix) - 1):
            temp.append([matrix[0][i], matrix[0][i + 1]])
        determinant(temp)
    else:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


m1 = [[2,5,3], [1,-2,-1], [1, 3, 4]]
print(determinant(m1))