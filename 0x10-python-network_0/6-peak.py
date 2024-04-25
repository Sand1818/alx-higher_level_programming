#!/usr/bin/python3
"""Find peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """list of unsorted integers"""
    if not list_of_integers:
        return None

    min = 0
    max = len(list_of_integers) - 1

    while min < max:
        midd = (min + max) // 2

        if list_of_integers[midd] > list_of_integers[midd + 1]:
            max = midd
        else:
            min = midd + 1

    return list_of_integers[min]
