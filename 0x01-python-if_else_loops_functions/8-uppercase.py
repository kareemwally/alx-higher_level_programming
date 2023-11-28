#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in str:
        if (ord(i) > 96 and ord(i) < 123):
            res += chr(ord(i) - 32)
        else:
            res += i
    print("{}".format(res))
