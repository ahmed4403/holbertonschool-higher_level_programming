#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string:
        result = 0
        index = 0
        for i in roman_string:
            if i == "I":
                result += 1
            elif i == "V":
                result += 5
            elif i == "X":
                result += 10
            elif i == "L":
                result += 50
            elif i == "C":
                result += 100
            elif i == "D":
                result += 500
            elif i == "M":
                result += 1000
        for j in roman_string:
            if j == "I" and roman_string[index + 1:2] == "V":
                result -= 2
            elif j == "I" and roman_string[index + 1:2] == "X":
                result -= 2
            elif j == "X" and roman_string[index + 1:2] == "L":
                result -= 20
            elif j == "X" and roman_string[index + 1:2] == "C":
                result -= 20
            elif j == "C" and roman_string[index + 1:2] == "D":
                result -= 200
            elif j == "C" and roman_string[index + 1:2] == "M":
                result -= 200
            index += 1
        return result
    return 0
