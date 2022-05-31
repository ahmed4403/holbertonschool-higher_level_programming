#!/usr/bin/python3
'''This is a module'''


def write_file(filename="", text=""):
    '''This is a function'''
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
