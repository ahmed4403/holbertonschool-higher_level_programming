#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    re = number % 10
else:
    re = number % -10
if re > 5:
    print("Last digit of", number, "is", re, "and is greater than 5")
if re == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, re))
if re < 6 and re != 0:
    print("Last digit of", number, "is", re, "and is less than 6 and not 0")
