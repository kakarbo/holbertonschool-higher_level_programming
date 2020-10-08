#!/usr/bin/python3
"""
 function that returns the number of lines of a text file:
"""


def number_of_lines(filename=""):
    """
    You must use the with statement
    You don’t need to manage file permission or
    file doesn't exist exceptions.
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        num_line = 0
        while True:
            line = myFile.readline()

            if not line:
                break

            num_line += 1
    return(num_line)
