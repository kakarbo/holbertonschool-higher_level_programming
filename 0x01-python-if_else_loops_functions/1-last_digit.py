#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
if number < 0:
    num = abs(number) % 10
    num = -num
print("Las digit of", number, "is", num, end=" ")
if num > 5:
    print("and is greater than 5")
elif num == 0:
    print("and is 0")
elif num < 6:
    print("and is less than 6 and not 0")