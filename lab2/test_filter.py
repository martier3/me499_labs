#!/usr/bin/env python3

from sensor import generate_sensor_data
from amp_filter import apply_amp_filter
import csv


n = 1000
data = generate_sensor_data(n,)
filter_data = apply_amp_filter(data, 0.8)
compile_data = (data, filter_data)

filename = "test_filter.csv"


with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(n):
        csvwriter.writerow(["{:.4f}".format(data[i]), "{:.4f}".format(filter_data[i])])
