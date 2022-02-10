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

def bigsim_gachapon(iterations):
    histo_data = []
    for i in range(iterations):
        number_of_boxes = simulate_gachapon(n)
        histo_data.append(number_of_boxes)
    return histo_data

gachapon_boxes = bigsim_gachapon(1000)

plt.figure(2)
plt.hist(gachapon_boxes, n)
plt.gca().set_xlim(left=0)
plt.xlabel('Number of Boxes')
plt.ylabel('Iterations')
plt.title('Number of Gachapon Boxes to get All Prizes')
plt.savefig('Problem2.png')
