#!/usr/bin/env python

def sum_i(*args):
    total = 0
    for i in args:
        total += i
    return total, print(total)

sum_i(1,2,3)

s = sum_i(1)

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))

def sum_r(numberlist):
   if len(numberlist) == 1:
        return numberlist[0]
   else:
       total = numberlist[0] + sum_r(numberlist[1:])
   return total

print(sum_r([1,3,5,7,9]))

s = sum_r([1])
