#!/usr/bin/python3
'''
This is a line of text
'''
import math


class MagicClass:
    '''
    This is a line of text
    '''
    def __init__(self, radius=0):
        '''
        This is a line of text
        '''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        '''
        This is a line of text
        '''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        '''
        This is a line of text
        '''
        return 2 * math.pi * self.__radius
