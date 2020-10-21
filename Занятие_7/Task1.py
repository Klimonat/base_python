class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result_str = ''
        for row in self.matrix:
            for elem in row:
                result_str += str(elem) + ' '
            result_str += "\n"
        return result_str

    def __add__(self, add_matrix):
        new_matrix_list = [[0 for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                new_matrix_list[i][j] = self.matrix[i][j] + add_matrix.matrix[i][j]
        return Matrix(new_matrix_list)

matrix_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
add_matrix_list = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
matrix = Matrix(matrix_list)
print(matrix)
add_matrix = Matrix(add_matrix_list)
print(add_matrix)

result = matrix + add_matrix
print(result)
