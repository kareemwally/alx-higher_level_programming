#!/usr/bin/python3
with open("zen.txt", 'r') as z:
    lis = z.read()
    s = lis.split('\n')
    for i in s:
        print(i)
