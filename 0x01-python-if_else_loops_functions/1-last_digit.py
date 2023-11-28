#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = ['and is greater than 5','and is 0','and is less than 6 and not 0']
if number < 0:
    number *= -1
if (number % 10) > 5:
    print("Last digit of {0} is {1} {2}".format(number, number % 10,s[0]))
elif (number % 10) == 0:
    print("Last digit of {0} is {1} {2}".format(number, number % 10, s[1]))
else :
    print("Last digit of {0} is {1} {2}".format(number, number % 10, s[2]))
