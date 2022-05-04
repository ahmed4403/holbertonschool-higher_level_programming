#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string:
        romanNums = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        prev = 0
        for i in reversed(roman_string):
            if romanNums[i] >= prev:
                result += romanNums[i]
            else:
                result -= romanNums[i]
            prev = romanNums[i]
        return result
    return 0
