#!/usr/bin/python3
'''
This is a line of text
write too many lines
for what is there
yes it is no it isn't
'''


def text_indentation(text):
    '''
    This is another line of text
    make sure that you....
    the lines must be long
    it is therefore have to be...
    '''
    if type(text) is not str:
        raise TypeError("text must be a string")
    newstr = 0
    for letter in text:
        if letter == " " and newstr == 0:
            continue
        newstr = 1
        if newstr == 1:
            if letter == "." or letter == "?" or letter == ":":
                print(f"{letter}\n")
                newstr = 0
            else:
                print(letter, end="")
