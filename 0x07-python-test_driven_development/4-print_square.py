#!/usr/bin/python3
'''
This is a line of text
write too many lines
for what is there
yes it is no it isn't
'''


def print_square(size):
    '''
    This is another line of text
    make sure that you....
    the lines must be long
    it is therefore have to be...
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for num in range(size):
        print(size * "#")
