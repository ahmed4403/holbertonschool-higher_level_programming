#!/usr/bin/python3
'''
This is a line of text
write too many lines
for what is there
yes it is no it isn't
'''


def say_my_name(first_name, last_name=""):
    '''
    This is another line of text
    make sure that you....
    the lines must be long
    it is therefore have to be...
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
