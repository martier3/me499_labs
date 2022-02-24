#!/usr/bin/env python

import numpy as np
from numpy import random
import matplotlib.pyplot as plt


def numpy_close(a=np.array([]), b=np.array([]), tol=np.exp(-8)):
    """
    Returns True if the arrays have the same shape and the absolute
    difference of each corresponding pair of elements is less than tol
    :param a: array in NumPy
    :param b: array in NumPy
    :param tol: float
    :return: if arrays are equal shape and abs(a-b) for each element
            is less than tol = True. else False
    """
    shape_a = np.shape(a)
    shape_b = np.shape(b)
    if shape_a == shape_b:
        c = abs(a - b)
        if c.all() <= tol:
            return True
        else:
            return False
    else:
        return False


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
    if start > end:
        raise ValueError
    else:
        x_values = np.linspace(start, end, num, endpoint=True)
        y_values = func(x_values)
        y_min = min(y_values)
        y_min_index = np.where(y_values == y_min)
        x_value_at_y_min = float(x_values[y_min_index])
    return x_value_at_y_min , y_min


def simulate_dice_rolls(num_rolls, iterations):
    """
    outputs a histogram of dice rolls
    :param num_rolls: number of dice rolls
    :param iterations: length of array
    :return: 1-D NumPy array of length iterations, where each item is the
            sum of throwing a fair 6-sided die num_rolls times.
    """

    sides_of_die = 6
    die_number_set = list(range(1, sides_of_die+1))
    random_rolls = np.random.randint(min(die_number_set), max(die_number_set)+1, iterations*num_rolls)
    num_roll_sort = np.reshape(random_rolls, (iterations, num_rolls))
    histo_array = np.sum(num_roll_sort, axis=1)

    plt.hist(histo_array,20)
    plt.savefig('dice_{}_rolls_{}.png'.format(num_rolls, iterations))

    return histo_array


def is_transformation_matrix(matrix=np.zeros((4,4))):
    """
    test matrix param to see if it is a valid transformation matrix
    :param matrix: 4x4 numpy array (rotation matrix)
    :return: boolean
    """
    r = matrix[0:3, 0:3]
    r_transpose = np.round(r.transpose(), 4)
    inverse = np.round(np.linalg.inv(r), 4)
    validity = (r_transpose == inverse)
    return bool(np.all(validity == True))


def nearest_neighbors(array=np.array([]), target_pt=np.array([]), dist=float()):
    """
    returns all the points in the array which are within Euclidean distance
    dist of point
    :param array: N x D Numpy array
    :param target_pt: 1D array of length D
    :param dist: threshold distance
    :return: M x D Numpy array where M < N
    """
    distance = np.linalg.norm(array-target_pt, axis=1)
    valid_indexes = list(*np.where(distance < dist))
    valid_array = array[valid_indexes, :]
    sorted_valid_distance_indices = np.argsort(np.linalg.norm(valid_array-target_pt, axis=1))
    sort_valid_array = valid_array[sorted_valid_distance_indices, :]
    return sort_valid_array
