#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator <a> <operator> <b>")
        sys.exit(1)
    a = argv[1]
    b = argv[3]
    operato = argv[2]
    if "+" == operato:
        print("{} {} {} = {}".format(a, operato, b, add(int(a), int(b))))
    elif "-" == operato:
        print("{} {} {} = {}".format(a, operato, b, sub(int(a), int(b))))
    elif "*" == operato:
        print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
    elif '/' == operato:
        print("{} {} {} = {}".format(a, operato, b, div(int(a), int(b))))
    else:
        print("Unknow operator. Available operators: +, -, * and /")
        sys.exit(1)
