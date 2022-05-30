#!/usr/bin/python3
'''This is a module'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''This is a class'''
    def __init__(self, width, height):
        '''This is a function'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''This is a function'''
        return self.__width * self.__height

    def __str__(self):
        '''This is a function'''
        return f"[Rectangle] {self.__width}/{self.__height}"
