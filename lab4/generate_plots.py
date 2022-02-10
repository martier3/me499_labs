#!/usr/bin/env python

from utils import *
import matplotlib.pyplot as plt
from counter import get_element_counts
import time

# Problem 1: Plot sping damper system
plt.figure(1)
plt.plot(t, state[:, 0])
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
plt.ylabel('Frequency of Number of Boxes Required')
plt.title('Number of Gachapon Boxes to get All Prizes')
plt.savefig('Problem2.png')

# Problem 3: Algorithmic runtimes

n_inputlist = list(range(50, 2550, 50))
times = []
lengths = []

for i in range(len(n_inputlist)):
    n = n_inputlist[i]
    list_of_numbers = random_list(n)
    lengths.append(len(list_of_numbers))
    start_time = time.time()
    get_element_counts(list_of_numbers)
    end_time = time.time()
    function_time = end_time-start_time
    times.append(function_time)

plt.figure(3)
plt.scatter(lengths, times)
plt.xlabel('List Length')
plt.ylabel('Time (sec)')
plt.title('Algorithmic Runtimes')
plt.savefig('Problem3.png')
