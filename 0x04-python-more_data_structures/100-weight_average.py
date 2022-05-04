#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        up = []
        down = []
        for i in my_list:
            up += [i[0] * i[1]]
        for j in my_list:
            down += [j[1]]
        result = sum(up) / sum(down)
        return float(result)
    return 0
