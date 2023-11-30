#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv) - 1
    print("{} arguments:".format(n) if n > 0 else "{} argument.".format(n))
    for i in range(1, n + 1):
        print("{}: {}".format(i, sys.argv[i]))
