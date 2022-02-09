#!/usr/bin/env python

# Problem 1: Plot sping damper system
import matplotlib.pyplot as plt
from utils import *

plt.plot(t, state[:,0])
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Time vs Displacement')
plt.savefig('Problem1.png')
