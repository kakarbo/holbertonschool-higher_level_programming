#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    d = '+'
    c = '='
    str = ("{} {} {} {} {}")
    print(str.format(a, d, b, c, add(a, b)))
    print(str.format(a, d, b, c, sub(a, b)))
    print(str.format(a, d, b, c, mul(a, b)))
    print(str.format(a, d, b, c, div(a, b)))
