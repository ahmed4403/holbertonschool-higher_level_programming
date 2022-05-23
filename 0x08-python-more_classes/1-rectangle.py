#!/usr/bin/python3
'''This is a module'''


class Rectangle:
    '''This is a class'''
    def __init__(self, width=0, height=0):
        '''This is a method'''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''This is a method'''
        return self.__width

    @width.setter
    def width(self, value):
        '''This is a method'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''This is a method'''
        return self.__height

    @height.setter
    def height(self, value):
        '''This is a method'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
