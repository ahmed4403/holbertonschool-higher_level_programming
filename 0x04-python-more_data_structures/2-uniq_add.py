#!/usr/bin/python3
def uniq_add(my_list=[]):
    newSet = set(my_list)
    tmp = 0
    for i in newSet:
        tmp = tmp + i
    return tmp
