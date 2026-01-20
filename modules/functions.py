# This module is exclusive for functions

def sum():
    print('this function will sum the values')

def multi():
    print('this function will multiplicate values')

def find_index(to_find, item):
    for i, value in enumerate(to_find):
        if value == item:
            return i
    return -1