#!/usr/bin/python3
with open("zen.txt", 'r') as z:
    l = list(z)
    for i in l:
        i = i.replace('\n', '')
        print(i)
