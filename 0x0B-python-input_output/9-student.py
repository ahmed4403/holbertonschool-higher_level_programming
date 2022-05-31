#!/usr/bin/python3
'''This is a moudle'''


class Student:
    '''This is a class'''
    def __init__(self, first_name, last_name, age):
        '''This is a method'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''This is a method'''
        return self.__dict__
