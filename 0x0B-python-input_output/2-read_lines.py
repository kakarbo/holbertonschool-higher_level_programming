#!/usr/bin/python3
"""
function that reads n lines of a text file (UTF8) and prints it to stdout:
"""


def read_lines(filename="", nb_lines=0):
    """
    Read the entire file if nb_lines is lower or equal to 0 OR greater or equal
    to the total number of lines of the file
    You must use the with statement
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        num_line = 1
        while True:
            
            line = myFile.readline()
            
            if nb_lines <= 0 or nb_lines >= num_line:
                print(line, end="")

            if not line:
                break

            num_line += 1
