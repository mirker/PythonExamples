#!/usr/bin/env python

def adder(good, bad, ugly, *other):
    ret = good + bad + ugly
    for i in other:
        ret += i

    return ret


print adder(1, 2, 3, 4, 5, 6)
#print adder()
print adder(1, 2, 0, *(7, 8, 9))
    
