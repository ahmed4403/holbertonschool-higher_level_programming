#!/usr/bin/python3
'''This is a module'''


def add_attribute(obj, att, value):
    '''This is a function'''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
