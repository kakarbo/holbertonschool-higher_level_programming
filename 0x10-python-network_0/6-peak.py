#!/usr/bin/python3
""" Task 6 - Function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Find a peak in a list of unsorted integers """
    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    low = 0
    high = len(list_of_integers) - 1
    while low < high:
        num = (low + high) // 2
        if list_of_integers[num] <= list_of_integers[num + 1]:
            low = num + 1
        elif list_of_integers[num] <= list_of_integers[num - 1]:
            high = num - 1
        elif (list_of_integers[num] >= list_of_integers[num + 1] and
              list_of_integers[num] >= list_of_integers[num - 1]):
            return list_of_integers[num]
    return list_of_integers[num]
