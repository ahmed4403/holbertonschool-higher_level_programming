#!/usr/bin/python3

def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for num in range(size):
        print(size * "#")
