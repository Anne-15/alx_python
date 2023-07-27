def square_matrix_simple(matrix=[]):
    def square_number(num):
        return num**2
    new_matrix = []
    for i in matrix:
        new_row = list(map(square_number, i))
        new_matrix.append(new_row)
    return new_matrix
