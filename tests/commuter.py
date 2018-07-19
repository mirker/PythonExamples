#!/usr/bin/env python

class Commuter:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print 'add', self.val, other
    def __radd__(self, other):
        print 'radd', self.val, other

if __name__ == '__main__':
    x = Commuter(88)
    y = Commuter(99)
    x+1
    1+y
    x+y
