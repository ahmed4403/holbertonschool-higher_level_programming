#!/usr/bin/python
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print(" ".join(f"{j}" for j in i))
