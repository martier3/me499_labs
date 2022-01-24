#!/usr/bin/env python


# Write a function called close(a, b, diff) in a file close.py, that takes
# three numbers as arguments. It returns True if the absolute difference between
# the first two numbers is less than the third number, e.g. the absolute value
# of a-b is less than diff


def close(a, b, diff):
    """
    :param a: first number
    :param b: second number
    :param diff: third number
    :return: if the abs dif of a-b is less than diff then True
    """
    difference = a - b
    if abs(difference) < diff:
        return True
    else:
        return False


test1 = close(5, 2, 1)
