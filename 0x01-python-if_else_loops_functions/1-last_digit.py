#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = ("Las digit of {} is {} {}")
lastdigit = int(repr(number)[-1])
if lastdigit > 5:
    print(str.format(number, lastdigit, "and is greater than 5"))
elif lastdigit == 0:
    print(str.format(number, lastdigit, "and is 0"))
else:
    print(str.format(number, lastdigit, "and is less than 6 and not 0"))