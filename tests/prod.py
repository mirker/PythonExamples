#!/usr/bin/env python

class Prod:
    def __init__(self, value):
        self.value = value
    def __call__(self, other):
        return self.value * other
    def comp(self, other):
        return self.value * other
    
if __name__ == '__main__':
    x = Prod(2)
    print x(3)
    print x(4)
    print x.comp(5)
    print x.comp(6)
