#!/usr/bin/env python

def sum_i(*args):
    total = 0
    for i in args:
        total += i
    return total, print(total)


s = sum_i(1)


def sum_r(*args):
   if len(args) == 1:
        return args[0]
   else:
       total = args[0] + sum_r(args[:1])
   return total


s = sum_r(1)
