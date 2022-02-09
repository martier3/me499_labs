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
    toy_list = [0, n-1]
    if toy_list not in prize_pool:
        prize_pool.append(random.randrange(0, n-1))
    else:
        return prize_pool, print(len(prize_pool)), print(len(toy_list))


simulate_gachapon(15)
