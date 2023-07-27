def square_matrix_simple(matrix=[]):
    def square_number(num):
        return num**2
    new_matrix = list(map(square_number, matrix))
    return new_matrix
