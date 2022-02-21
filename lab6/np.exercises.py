#!/usr/bin/env python

import numpy as np

def numpy_close(a, b, tol = np.exp(-8)):
    """
    :param a: array in NumPy
    :param b: array in NumPy
    :param tol: float
    :return: if arrays are equal shape and abs(a-b) for each element
            is less than tol = True. else False
    """
    if a.shape == b.shape:
        print(a)
        print(b)
        c = abs(a - b)
        if c.all() <= tol:
            return True, print(True)
    else:
        return False, print(False)

