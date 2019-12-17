#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    d = []
    for i in my_list:
        if i % 2 == 0:
            d.append(True)
        else:
            d.append(False)
    return d
