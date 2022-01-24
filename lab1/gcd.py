#!/usr/bin/env python

# In a new file called gcd.py write a function called gcd that calculates the
# greatest common divisor fo two numbers, gcd(a,b).

# The function must use Euclid's algorithm. It should take two numbers as input
# and return their greatest common divisor.
from math import gcd as pygcd

import random


def gcd(a, b):
    while b:
        [a, b] = [b, a % b]
        """
        1) 'b' on right side becomes 'a' on left side
        2) 'a%b' is the remainder of a/b and takes the place of 'b' on the left side
        3) while loop iterates until 'b' = 0
        4) function outputs 'a' as the gcd
        """
    return a


print(gcd(10, 40))
print(gcd(40, 10))


def gcd_test():
    iteration = 1
    while iteration < 1000:
        a = random.randint(1, 10000)
        b = random.randint(1, 10000)
        test = pygcd(a, b)
        mine = gcd(a, b)
        if test == mine:
            iteration = iteration + 1
        else:
            return False
    return True


gcd_test()
