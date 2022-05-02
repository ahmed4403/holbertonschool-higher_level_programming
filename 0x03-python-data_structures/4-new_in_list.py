#!/usr/bin/python
def new_in_list(my_list, idx, element):
    listDup = my_list.copy()
    if idx < 0:
        return listDup
    if idx > len(my_list) - 1:
        return listDup
    listDup[idx] = element
    return listDup
