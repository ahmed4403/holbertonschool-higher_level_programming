#!/usr/bin/python3
'''
This is a line of text
write too many lines
for what is there
yes it is no it isn't
'''


def add_integer(a, b=98):
    '''
    This is another line of text
    make sure that you....
    the lines must be long
    it is therefore have to be...
    '''
    if type(a) is not int and type(a) is not float or a != a or \
       a == float("inf") or a == float("-inf"):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float or b != b or \
       b == float("inf") or b == float("-inf"):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
