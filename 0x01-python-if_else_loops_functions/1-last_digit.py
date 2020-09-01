#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    num = number % 10
else:
    num = number % -10
string = "Last digit of {} is {} and is {}"
if num > 5:
    print(string.format(number, num, "greater than 5"))
elif num == 0:
    print(string.format(number, num, "0"))
elif num < 6:
    print(string.format(number, num, "less than 6 and not 0"))
