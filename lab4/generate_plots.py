#!/usr/bin/env python

from utils import *
import matplotlib.pyplot as plt

# Problem 1: Plot sping damper system
plt.figure(1)
plt.plot(t, state[:,0])
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Time vs Displacement')
plt.savefig('Problem1.png')

# Problem 2: Histogram of the gachapon problem
n = 15
plt.figure(2)
plt.hist(simulate_gachapon(n), n)
plt.savefig('Problem2.png')
