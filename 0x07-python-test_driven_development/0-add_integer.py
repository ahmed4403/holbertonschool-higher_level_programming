#!/usr/bin/python3

def add_integer(a, b=98):
    if type(a) is not int and type(a) is not float or a != a or \
       a == float("inf") or a == float("-inf"):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float or b != b or \
       b == float("inf") or b == float("-inf"):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
