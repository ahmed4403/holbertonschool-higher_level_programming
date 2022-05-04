#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    newSet_1 = set_1.difference(set_2)
    newSet_2 = set_2.difference(set_1)
    return newSet_1.union(newSet_2)
