#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in str:
        if not (ord(i) > 64 and ord(i) < 91):
            res += chr(ord(i) - 32)
        else:
            res += i
    print("{}".format(res))
