#!/usr/bin/python3
if __name__ == "__main__":
    import math, sys
    res = 0
    for i in range(1, len(sys.argv)):
        print("{}".format(sys.argv[i]))
        res += int(sys.argv[i])
    print(res)
