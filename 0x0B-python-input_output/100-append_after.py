#!/usr/bin/python3
'''This is a moudle'''


def append_after(filename="", search_string="", new_string=""):
    '''This is a function'''
    new = ""
    with open(filename) as f:
        for line in f:
            new += line
            if search_string in line:
                new += new_string
    with open(filename, "w") as ff:
        ff.write(new)
