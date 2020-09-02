#!/usr/bin/python3
def fizzbuzz():
    """function that prints the numbers from 1 to 100 separated by a space."""
    for i in range(1, 100):
        if i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 10 == 0:
            print("FizzBuzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
