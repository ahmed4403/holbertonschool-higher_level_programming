#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string:
        n = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev = 0
        for i in reversed(roman_string):
            if n[i] >= prev:
                result += n[i]
            else:
                result -= n[i]
            prev = n[i]
        return result
    return 0
