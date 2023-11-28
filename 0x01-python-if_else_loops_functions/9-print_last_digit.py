#!/usr/bin/python3
def print_last_digit(number):
    x = 0
    if number < 0:
        x = (-1 * number % 10)
    else:
        x = number % 10
    print(x, end='')
    return x
