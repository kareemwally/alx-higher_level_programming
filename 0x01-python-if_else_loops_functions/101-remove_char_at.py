#!/usr/bin/python3
def remove_char_at(str, n):
    res = ""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            res+=str[i]
    return res
print(remove_char_at("Best School", 3))

