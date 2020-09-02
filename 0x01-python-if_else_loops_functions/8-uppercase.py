#!/usr/bin/python3
def uppercase(str):
    """FUNCTION THAT PRINTS A STRING IN UPPERCASE FOLLOWED BY A NEW LINE"""
    str1 = list(str)
    for i in range(len(str1)):
        if (ord(str1[i]) > 96 and ord(str1[i]) < 123):
            str1[i] = chr(ord(str1[i]) - 32)
    print("{}".format(("").join(str1)))
