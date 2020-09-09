#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    cadena = ''
    for i in matrix:
        cadena = cadena + '\n'
        for a in i:
            cadena = cadena + "{:d} ".format(a)
        cadena = cadena[:-1]
    print(cadena[1:])
