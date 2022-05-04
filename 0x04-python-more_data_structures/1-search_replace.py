#!/usr/bin/python3
def search_replace(my_list, search, replace):
    j = 0
    newList = my_list.copy()
    for i in newList:
        if i == search:
            newList[j] = replace
        j = j + 1
    return newList
