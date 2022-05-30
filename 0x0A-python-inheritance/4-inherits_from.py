#!/usr/bin/python3
'''This is a moudle'''


def inherits_from(obj, a_class):
    '''This is a function'''
    return issubclass(type(obj), a_class) and type(obj) is not a_class
