#!/usr/bin/env python

def adder(val1, val2, *others):
    val = val1 + val2
    for i in others:
        val = val + i
    return val

test1 = 1
test2 = 2
test3 = 3

print adder(1, 2, 3, 4, 5, 6, 7, 8)
print adder([1, 2], [3, 4], ['ab', 'c'])
print adder({1:'a', 2:'b'}, {'a':1, 'b':2})
