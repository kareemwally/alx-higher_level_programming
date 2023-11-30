#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    if n == 1:
        print("{} argument:".format(n))
    elif not n:
        print("{} arguments.".format(n))
    else:
        print("{} arguments:".format(n))
    for i in range(1, n + 1):
        print("{}: {}".format(i, sys.argv[i]))
