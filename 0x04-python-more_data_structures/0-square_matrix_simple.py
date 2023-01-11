def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    return list(map(lambda x: map(lambda y: y ** 2, x), new_matrix)