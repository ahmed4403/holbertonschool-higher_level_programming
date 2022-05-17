#!/usr/bin/python3
'''
This is a line of text
'''


class Square:
    '''
    This is another line of text
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Well look at this, this is another
        line of text
        '''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        if type(position) is not tuple or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

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

    def my_print(self):
        '''
        This is a line of text
        '''
        m = 0
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            for k in range(self.__size):
                while m < self.__position[0]:
                    print(" ", end="")
                    m += 1
                print("#", end="")
            m = 0
            print()

    @property
    def position(self):
        '''
        This is a line of text
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        This is a line of text
        '''
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
