#!/usr/bin/python3
def print_last_digit(number):
    """FUNCTION THAT PRINTS THE LAST DIGIT OF A NUMBER"""
    num = int(repr(number)[-1])
    print(num, end='')
    return (num)
