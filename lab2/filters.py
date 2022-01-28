#!/usr/bin/env python


from sensor import generate_sensor_data
from amp_filter import apply_amp_filter
import csv

n = 1000
data = generate_sensor_data(n,)
filter_data = apply_amp_filter(data, 0.8)

def mean_filter():
    """
    Apply a mean filter to an iterable, returning a list.
    """
    for i in range(n):

    return mean_filter


filename = "filter.csv"

with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(n):
        csvwriter.writerow(["{:.4f}".format(data[i]), "{:.4f}".format(filter_data[i]), "{:.4f}".format(mean_filter[i])])
