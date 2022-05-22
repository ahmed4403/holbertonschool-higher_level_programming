#!/usr/bin/python3
'''
This is a line of text
write too many lines
for what is there
yes it is no it isn't
'''


def matrix_divided(matrix, div):
    '''
    This is another line of text
    make sure that you....
    the lines must be long
    it is therefore have to be...
    '''
    if type(matrix) is not list or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    idx = 0
    for i in matrix:
        if type(i) is not list or not matrix[idx]:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        idx += 1
    for j in matrix:
        for k in j:
            if type(k) is not int and type(k) is not float or k != k or \
               k == float("inf") or k == float("-inf"):
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float or div != div or \
       div == float("inf") or div == float("-inf"):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in listM] for listM in matrix]
