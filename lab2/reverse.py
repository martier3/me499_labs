#!/usr/bin/env python

def reverse_i(list_input):
    reverse_of_input = []
    for item in list_input:
        reverse_of_input.insert(0, item)
    return reverse_of_input, print(reverse_of_input)


reverse_i(['h','e','l','l','o'])
reverse_i([1,2,3,4,5,6,7,8,9])

def reverse_r(list_input):
    if len(list_input) == 0:
        return list_input
    else:
        #print(list_input)
        #print above shows the recursive step by step
        return reverse_r(list_input[1:])+list_input[:1]

print(reverse_r(['h','e','l','l','o']))
