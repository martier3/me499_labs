#!/usr/bin/env python

from utils import *
import matplotlib.pyplot as plt
import numpy as np

# Problem 1: Plot sping damper system
plt.figure(1)
plt.plot(t, state[:,0])
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Time vs Displacement')
plt.savefig('Problem1.png')

# Problem 2: Histogram of the gachapon problem
n = 15

def bigsim_gachapon(iterations):
    histo_data = []
    for i in range(iterations):
        new_numbers = simulate_gachapon(n)
        histo_data = histo_data + new_numbers
    return histo_data, print(len(histo_data)), print(histo_data)

plt.figure(2)
plt.hist(bigsim_gachapon(1000), n)
plt.savefig('Problem2.png')
