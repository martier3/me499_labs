import numpy as np
import math
import random

def compute_inertia_matrix(array=np.array([]), mass=1):
    n = np.shape(array)[0]
    m = mass/n
    adjustment_array = np.array([[1, -1, -1],
                                 [-1, 1, -1],
                                 [-1, -1, 1]])
    inertia_array = np.zeros([3, 3])
    for row in array:
        x = row[0]
        y = row[1]
        z = row[2]
        inertia_array_per_row = np.array([[m*(y**2 + z**2), m*x*y, m*x*z],
                                            [m*x*y, m*(x**2 + z**2), m*y*z],
                                            [m*x*z, m*y*z, m*(x**2 + y**2)]])
        inertia_array = np.add(inertia_array_per_row, inertia_array)
    return np.multiply(inertia_array, adjustment_array)


def sample_sphere_polar(N):
    r = 1
    i = 0
    sphere_points = np.empty((0,3))
    while i <= N-1:
        phi = random.uniform(0, math.pi)
        theta = random.uniform(0, 2 * math.pi)
        x = np.array(r*math.sin(phi)*math.cos(theta))
        y = np.array(r*math.sin(phi)*math.sin(theta))
        z = np.array(r*math.cos(phi))
        sphere_points = np.append(sphere_points, np.array([[x,y,z]]), axis=0)
        i += 1
    return np.array(sphere_points)


def sample_sphere_gaussian(N):
    i = 0
    sphere_points = np.empty((0, 3))
    while i <= N-1:
        vector = [np.random.normal() for _ in range(3)]
        normalized_vector = vector / np.linalg.norm(vector)
        sphere_points = np.append(sphere_points, [normalized_vector], axis=0)
        i += 1
    return np.array(sphere_points)


def test_inertia_matrices_output():
    m = 1
    r = 1
    n =1000
    polar = compute_inertia_matrix(sample_sphere_polar(n))
    gaussian = compute_inertia_matrix(sample_sphere_gaussian(n))
    expected = np.array([[(2 / 3) * m * (r ** 2), 0, 0],
                        [0, (2 / 3) * m * (r ** 2), 0],
                        [0, 0, (2 / 3) * m * (r ** 2)]])
    np.set_printoptions(precision=3, suppress=True)
    return print('Polar:\n', polar, '\nGaussian:\n', gaussian, '\nExpected:\n', expected)
