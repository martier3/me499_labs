#!/usr/bin/env python

def sum_i(*args):
    total = 0
    for i in args:
        total += i
    return total, print(total)

sum_i(1,2,3)

s = sum_i(1)


def sum_r(*args):
   if len(args) == 1:
        return args[0]
   else:
       total = args[0] + sum_r(args[:1])
   return total

print(sum_r([1,2,3,4,5,6]))

s = sum_r(1)
print(s)
