#!/usr/bin/env python

def sum_i(*args):
    total = 0
    for i in args:
        total += i
    return total, print(total)

sum_i(1,2,3)

s = sum_i(1)

def sum_r(*args):
    n = 0
    if n == 1:
        return 0
    else:
        return (n+sum_r(*args-1)), print(sum_r)

sum_r(1,2,3)
