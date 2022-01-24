#!/usr/bin/env python

# Take the code you wrote for calculating the volume of a cylinder and put it
# into a function, so you can reuse it. Create a file called volumes.py and write
# a function called cylinder_volume(radius, height) that returns the volume of
# the corresponding cylinder.

# cylinder volume calculation
# V=math.pi*(r**2)*(h)

import math


def cylinder_volume(radius, height):
    """
    this function calculates
    the volume of a cylinder
    """
    if radius <= 0:
        print('inputs must be positive')
        raise ValueError
    elif height <= 0:
        print('inputs must be positive')
        raise ValueError
    else:
        volume = math.pi * (radius ** 2) * height
    return volume


test_cylinder = cylinder_volume(3, 5)
print(test_cylinder)
"""
The following inputs are tests for negative inputs
to show the ValueError exception
"""
# test_cylinder_error = cylinder_volume(-3, 5)
# print(test_cylinder_error)


def torus_volume(inner_rad, outer_rad):
    """
    this function calculates
    the volume of a torus
    """
    if inner_rad >= outer_rad:
        print('inputs must be positive')
        raise ValueError
    elif outer_rad <= 0:
        print('inputs must be positive')
        raise ValueError
    elif inner_rad <= 0:
        print('inputs must be positive')
        raise ValueError
    else:
        minor_radius = (outer_rad - inner_rad) / 2
        major_radius = (outer_rad + inner_rad) / 2

    (math.pi * (minor_radius ** 2)) * (2 * math.pi * major_radius)

    return (math.pi * (minor_radius ** 2)) * (2 * math.pi * major_radius)


test_torus = torus_volume(3, 4)
print(test_torus)
"""
The following inputs are tests for negative inputs
to show the ValueError exception
"""
# test_torus_error = torus_volume(-3, 4)
# print(test_torus_error)
