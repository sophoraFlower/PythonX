

class Matrix(object):
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.m = len(data[0])


def mat_mul(matrix_1: Matrix, matrix_2: Matrix):
    # assert matrix_1.m == matrix_2.n
    n, m, s = matrix_1.n, matrix_1.m, matrix_2.m
    result = [[0 for _ in range(n)] for _ in range(s)]
    print(result)
    for i in range(n):
        for j in range(s):
            for k in range(m):
                result[i][k] += matrix_1.data[i][j] * matrix_2.data[j][k]

    return Matrix(result)


a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])
print(mat_mul(a, b).data)
