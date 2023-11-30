#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys
    n = len(sys.argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        m = int(sys.argv[1])
        n = int(sys.argv[3])
        operand = sys.argv[2]
        print("{} {} {} ".format(m, operand, n), end = '')
        if operand == '+':
            print("= {}".format(add(m, n)))
        elif operand == '-':
            print("= {}".format(sub(m, n)))
        elif operand == '/':
            print("= {}".format(div(m, n)))
        elif operand == '*':
            print("= {}".format(mul(m, n)))
        
