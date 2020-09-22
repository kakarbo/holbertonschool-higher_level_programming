#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            resutl += (a**b) / i
        except:
            resutl = b + a
            break
    return(resutl)
