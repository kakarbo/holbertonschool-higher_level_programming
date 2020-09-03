#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0 or i % 5 == 0:
            if a % 3 != 0:
                print("Fizz", end=' ')
            elif a % 5 != 0:
                print("Buzz", end=' ')
            else:
                print("FizzBuzz", end=' ')
        else:
            print("{}".format(a), end=' ')
