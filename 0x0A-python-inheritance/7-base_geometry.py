#!/usr/bin/python3
'''This is a module'''


class BaseGeometry:
    '''This is a class'''
    def area(self):
        '''This is a function'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''This is a function'''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
