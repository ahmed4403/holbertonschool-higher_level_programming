#!/usr/bin/python3
def no_c(my_string):
    count = 0
    for i in my_string:
        if i == "c" or i == "C":
            new = my_string[0:count] + my_string[count + 1:]
            return new
        count = count + 1
    return my_string
