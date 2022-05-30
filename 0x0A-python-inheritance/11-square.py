#!/usr/bin/python3
'''This is a module'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''This is a class'''
    def __init__(self, size):
        '''This is a function'''
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        '''This is a function'''
        return self.__size ** 2

    def __str__(self):
        '''This is a function'''
        return f"[Rectangle] {self.__size}/{self.__size}"
