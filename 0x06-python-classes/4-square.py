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
        self.__size = size

    def area(self):
        '''
        Line after line after line of text
        for the "project"
        '''
        return self.__size * self.__size

    @property
    def size(self):
        '''
        This is a line of text
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        This is a line of text
        '''
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
