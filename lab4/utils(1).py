#!/usr/bin/env python

import numpy as np

# Problem 1: Plot spring damper system
from msd import *

m = 1.0
k = 5.0
c = 2.5
x = 1
x_dot = -1
t = 40.0
dt = 0.1

smd = MassSpringDamper(m, k, c)
state, t = smd.simulate(x, x_dot, t, dt)

# Problem 2: Histogram of the gachapon problem

np.random.seed()

def simulate_gachapon(n):

    prize_pool = []
    toy_list = list(range(0, n))
    while all(item in prize_pool for item in toy_list) is False:
        add_number = np.random.randint(0, n)
        prize_pool.append(add_number)
    else:
        return len(prize_pool)


# Problem 3: Algorithmic runtimes

def random_list(n):
    random_numbers = []
    for i in range(n):
        random_numbers.append(np.random.randint(0, n))
    return random_numbers

