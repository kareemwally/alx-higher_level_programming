#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    mul = 0
    for i, k in my_list:
        sum += k
        mul += i * k
    return sum / mul
