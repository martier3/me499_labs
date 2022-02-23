#!/usr/bin/env python

import numpy as np
from numpy import random
import matplotlib.pyplot as plt


def numpy_close(a, b, tol=np.exp(-8)):
    """
    Returns True if the arrays have the same shape and the absolute
    difference of each corresponding pair of elements is less than tol
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


def simple_minimizer(func, start=float(), end=float(), num=100):
    """
    function evaluates func at num evenly-spaced points between
    start and end (endpoint inclusive) and return two values:
        The x corresponding to the minimum value of f(x)
        The minimum f(x)
    :param func: function input
    :param start: float start of search region
    :param end: float end of search region
    :param num: total number of evenly spaced points to search
    :return:
    """
    x_values = np.linspace(start, end, num)
    min = func.min(x_values)
    x_min = x_values[func[min]]
    return x_min, min


def simulate_dice_rolls(num_rolls, iterations):
    """
    outputs a histogram of dice rolls
    :param num_rolls: number of dice rolls
    :param iterations: length of array
    :return: 1-D NumPy array of length iterations, where each item is the
            sum of throwing a fair 6-sided die num_rolls times.
    """
    histo_array = ([])
    sum_roll_array = np.empty(iterations, dtype=int)
    sides_of_die = 6
    for n in range(iterations):
        die_array = np.arange(1, sides_of_die+1, 1)
        all_rolls_array = np.empty(num_rolls, dtype=int)
        for i in range(num_rolls):
            roll = random.choice(die_array)
            all_rolls_array[i] = roll
        sum_roll_array[n] = all_rolls_array.sum()
        histo_array = np.concatenate([histo_array, all_rolls_array])
    d = np.diff(np.unique(histo_array)).min()
    left_of_first_bin = histo_array.min() - float(d) / 2
    right_of_last_bin = histo_array.max() + float(d) / 2
    plt.hist(histo_array, np.arange(left_of_first_bin, right_of_last_bin + d, d))
    plt.savefig('dice_{}_rolls_{}.png'.format(num_rolls, iterations))
    return sum_roll_array


def is_transformation_matrix(matrix=np.zeros((4,4))):
    """
    test matrix param to see if it is a valid transformation matrix
    :param matrix: 4x4 numpy array (rotation matrix)
    :return: boolean
    """
    r = matrix[0:3, 0:3]
    r_transpose = r.transpose()
    identity = np.identity(3)
    inverse = r_transpose @ r
    validity = bool((identity == inverse).all())
    return validity


def nearest_neighbors(array=np.array([]), target_pt=np.array([]), dist=float()):
    """
    returns all the points in the array which are within Euclidean distance
    dist of point
    :param array: N x D Numpy array
    :param target_pt: 1D array of length D
    :param dist: threshold distance
    :return: M x D Numpy array where M < N
    """
    i = 0
    valid_rows = []
    for row in array:
        if abs(np.linalg.norm(row - target_pt)) < abs(dist):
            valid_rows.append(i)
        i += 1
    row_indices = np.array(valid_rows)
    return array[row_indices, :]
