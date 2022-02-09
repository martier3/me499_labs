#!/usr/bin/env python

from utils import *
import matplotlib.pyplot as plt
import numpy as np

# Problem 1: Plot sping damper system
plt.plot(t, state[:,0])
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Time vs Displacement')
plt.savefig('Problem1.png')

# Problem 2: Histogram of the gachapon problem
n_bins = 15
plt.hist(simulate_gachapon(15), density=1, bins=n_bins)
plt.show()
