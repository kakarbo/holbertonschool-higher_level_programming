#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = ("Las digit of {} is {} {}")
num = number % 10
if number < 0:
    num = abs(number) % 10
    num = -num
if num > 5:
    print(str.format(number, num, "and is greater than 5"))
elif num == 0:
    print(str.format(number, num, "and is 0"))
if num < 6 and num != 0:
    print(str.format(number, num, "and is less than 6 and not 0"))
