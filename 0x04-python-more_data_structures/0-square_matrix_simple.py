#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matriz[i][j] = new_matrix[i][j]**2
    return(matriz)
