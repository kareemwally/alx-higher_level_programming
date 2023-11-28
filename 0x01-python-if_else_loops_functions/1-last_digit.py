#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = ['and is greater than 5', 'and is 0', 'and is less than 6 and not 0']
num = number % 10
if number < 0:
    num = -1 * ((number * -1) % 10)
if num > 5:
    print("Last digit of {0} is {1} {2}".format(number, num, s[0]))
elif not num:
    print("Last digit of {0} is {1} {2}".format(number, num, s[1]))
else:
    print("Last digit of {0} is {1} {2}".format(number, num, s[2]))
