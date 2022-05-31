#!/usr/bin/python3
'''This is a module'''


def read_file(filename=""):
    '''This is a function'''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
