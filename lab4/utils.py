#!/usr/bin/env python

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
import random

def simulate_gachapon(n):
    prize_pool = []
    toy_list = list(range(0, n))
    print(toy_list)
    while all(item in prize_pool for item in toy_list) is False:
        add_number = random.randrange(0, n)
        prize_pool.append(add_number)
    else:
        return prize_pool
