#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    name = next(iter(a_dictionary))
    biggest = a_dictionary.get(name)
    for key, value in a_dictionary.items():
        if value > biggest:
            biggest = value
            name = key
    return name
