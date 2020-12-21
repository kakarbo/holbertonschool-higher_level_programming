#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers. """
    list1 = list_of_integers
    if not list1:
        return(None)
    elif len(list1) == 1:
        return(list1[0])
    low = 0
    high = len(list1) - 1
    while low < high:
        num = (low + high) // 2
        if list1[num] <= list1[num + 1]:
            low = num + 1
        elif list1[num] <= list1[num - 1]:
            low = num - 1
        elif (list1[num] >= list1[num + 1] and
              list1[num] >= list1[num - 1]):
            return(list1[num])
    return(list1[low])
