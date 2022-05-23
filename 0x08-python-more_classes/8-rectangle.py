#!/usr/bin/python3
'''This is a module'''


class Rectangle:
    '''This is a class'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''This is a method'''
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        '''This is a method'''
        return self.__width * self.__height

    def perimeter(self):
        '''This is a method'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        '''This is a method'''
        if self.__width == 0 or self.__height == 0:
            return ""
        seq = ""
        st = str(self.print_symbol)
        for i in range(self.__height):
            seq += st * self.__width
            if i != self.__height - 1:
                seq += "\n"
        return seq

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''This is a method'''
        print("Bye rectangle...")

    def __del__(self):
        '''This is a method'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''This is a method'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
