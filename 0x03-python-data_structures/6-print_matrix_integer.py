#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    for row in range(rows):
        values = len(matrix[row])
        for val in range(values):
            if (val != values - 1):
                print("{:d}".format(matrix[row][val]), end=" ")
            else:
                print("{:d}".format(matrix[row][val]))
