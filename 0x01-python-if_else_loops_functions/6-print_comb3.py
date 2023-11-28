#!/usr/bin/python3
i = 1
count = 2
while i < 89:
    if not i % 10:
        i = i+count
        count += 1
    if i == 89:
        break
    print("{0:02d}".format(i), end=', ')
    i += 1
print(i)
