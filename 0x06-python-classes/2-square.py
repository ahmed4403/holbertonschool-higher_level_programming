#!/usr/bin/python3
'''
This is a line of text
'''


class Square:
    '''
    This is another line of text
    '''
    def __init__(self, size=0):
        '''
        Well look at this, this is another
        line of text
        '''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
