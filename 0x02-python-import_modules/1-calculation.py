#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    str0 = ("{} + {} = {}")
    str1 = ("{} - {} = {}")
    str2 = ("{} * {} = {}")
    str3 = ("{} / {} = {}")
    print(str0.format(a, b, add(a, b)))
    print(str1.format(a, b, sub(a, b)))
    print(str2.format(a, b, mul(a, b)))
    print(str3.format(a, b, div(a, b)))
