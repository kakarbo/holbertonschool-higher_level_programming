#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = argv[1]
    b = argv[3]
    operator = argv[2]
    if "+" == operator:
        print("{} {} {} = {}".format(a, operator, b, add(int(a), int(b))))
    elif "-" == operator:
        print("{} {} {} = {}".format(a, operator, b, sub(int(a), int(b))))
    elif "*" == operator:
        print("{} {} {} = {}".format(a, operator, b, mul(int(a), int(b))))
    elif '/' == operator:
        print("{} {} {} = {}".format(a, operator, b, div(int(a), int(b))))
    else:
        print("Unknow operator. Available operators: +, -, * and /")
        sys.exit(1)
