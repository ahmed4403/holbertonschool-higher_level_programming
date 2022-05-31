#!/usr/bin/python3
'''This is a module'''


def append_write(filename="", text=""):
    '''This is a function'''
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
