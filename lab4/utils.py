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
